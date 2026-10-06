import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

try:
    from adjustText import adjust_text
    HAS_ADJUST_TEXT = True
except ImportError:
    HAS_ADJUST_TEXT = False


def _order_layers(G, layers_sorted, layer_nodes, sort_by, n_sweeps=4):
    """
    Decide the vertical ordering of nodes within each layer.

    'barycenter' iteratively reorders each layer by the average
    position of its neighbors in adjacent layers (forward + backward
    sweeps), which is the standard trick for reducing edge crossings
    in layered/multipartite graph drawings.
    """
    order = {layer: list(nodes) for layer, nodes in layer_nodes.items()}

    if sort_by == 'degree':
        for layer in layers_sorted:
            order[layer].sort(key=lambda n: G.degree(n), reverse=True)
        return order

    if sort_by is None:
        return order

    # --- barycenter heuristic ---
    for layer in layers_sorted:
        order[layer].sort(key=lambda n: G.degree(n), reverse=True)

    pos_index = {
        layer: {n: i for i, n in enumerate(order[layer])}
        for layer in layers_sorted
    }

    # Edges only ever connect layer i -> layer i+1 (source_type, target_type)
    # e.g. MicroRNA -> Messenger RNA -> Semantics -> Pathway, with no
    # skip-layer or reverse edges. That means, for any node, its
    # predecessors are guaranteed to sit in the previous layer and its
    # successors in the next layer -- no subset filtering needed.
    for _ in range(n_sweeps):
        # forward sweep: order layer i by its predecessors (layer i-1)
        for layer in layers_sorted[1:]:
            prev_layer = layer - 1

            def bary(n, prev_layer=prev_layer, layer=layer):
                nbrs = list(G.predecessors(n))
                if not nbrs:
                    return pos_index[layer][n]
                return np.mean([pos_index[prev_layer][nb] for nb in nbrs])

            order[layer].sort(key=bary)
            pos_index[layer] = {n: i for i, n in enumerate(order[layer])}

        # backward sweep: order layer i by its successors (layer i+1)
        for layer in reversed(layers_sorted[:-1]):
            next_layer = layer + 1

            def bary(n, next_layer=next_layer, layer=layer):
                nbrs = list(G.successors(n))
                if not nbrs:
                    return pos_index[layer][n]
                return np.mean([pos_index[next_layer][nb] for nb in nbrs])

            order[layer].sort(key=bary)
            pos_index[layer] = {n: i for i, n in enumerate(order[layer])}

    return order


def _validate_adjacent_layer_edges(G, source_col, target_col, edges):
    """
    Confirm every edge connects layer i -> layer i+1 (e.g. MicroRNA ->
    Messenger RNA, Messenger RNA -> Semantics, Semantics -> Pathway).
    The barycenter ordering above relies on this; a skip-layer or
    reversed edge would silently distort the layout rather than error,
    so it's worth catching explicitly.
    """
    bad = []
    for u, v in edges[[source_col, target_col]].itertuples(index=False, name=None):
        if G.nodes[v]['subset'] - G.nodes[u]['subset'] != 1:
            bad.append((u, v, G.nodes[u]['node_type'], G.nodes[v]['node_type']))

    if bad:
        examples = '\n'.join(
            f'  {u!r} ({ut}) -> {v!r} ({vt})' for u, v, ut, vt in bad[:10]
        )
        raise ValueError(
            f'{len(bad)} edge(s) do not connect consecutive layers '
            '(expected source layer -> target layer = source layer + 1, '
            'e.g. MicroRNA -> Messenger RNA -> Semantics -> Pathway).\n'
            f'Examples:\n{examples}'
        )


def plot_multipartite_network(
    edges,
    nodes,
    source_col='source',
    target_col='target',
    node_col='id',
    type_col='type',
    label_col='id',
    figsize=(24, 14),
    layer_gap=3.0,
    node_gap=1.0,
    layer_node_gaps=None,          # optional dict {layer_index: node_gap} to override
                                    # node_gap for specific (e.g. dense) layers
    sort_by='barycenter',          # 'barycenter', 'degree', or None
    node_size_by_degree=True,
    min_node_size=15,
    max_node_size=350,
    label_top_n=None,              # label only the top-N nodes by degree, per layer
    label_min_degree=None,         # or: label only nodes with degree >= this
    font_size=7,
    avoid_label_overlap=True,
    save_path='lqn.png',
    dpi=150,
):
    """
    Plot a multipartite network with reduced clutter for dense layers.

    Labeling control (pick one, or neither to label everything):
        label_top_n=15        -> label the 15 highest-degree nodes per layer
        label_min_degree=3    -> label any node with degree >= 3
    """
    layer_map = {
        'MicroRNA': 0,
        'Messenger RNA': 1,
        'Semantics': 2,
        'Pathway': 3,
    }

    color_map = {
        'MicroRNA': '#1f77b4',
        'Messenger RNA': '#ff7f0e',
        'Semantics': '#2ca02c',
        'Pathway': '#d62728',
    }

    G = nx.DiGraph()

    # ------------------------------------------------------------
    # Add nodes with multipartite layer information
    # ------------------------------------------------------------
    for _, row in nodes.iterrows():
        node_type = row[type_col]

        if node_type not in layer_map:
            raise ValueError(
                f'Unknown node type {node_type!r}. '
                f'Expected one of {list(layer_map)}'
            )

        G.add_node(
            row[node_col],
            subset=layer_map[node_type],
            node_type=node_type,
            label=row[label_col] if label_col else row[node_col],
        )

    # ------------------------------------------------------------
    # Check that all edge nodes exist
    # ------------------------------------------------------------
    edge_nodes = set(edges[source_col]) | set(edges[target_col])
    missing_nodes = edge_nodes - set(G.nodes)

    if missing_nodes:
        raise ValueError(
            f'{len(missing_nodes)} nodes in edges are missing '
            'from the nodes dataframe.\n'
            f'Examples: {list(missing_nodes)[:10]}'
        )

    # ------------------------------------------------------------
    # Add edges
    # ------------------------------------------------------------
    G.add_edges_from(
        edges[[source_col, target_col]].itertuples(index=False, name=None)
    )

    # Edges are expected to only ever connect consecutive layers
    # (MicroRNA -> Messenger RNA -> Semantics -> Pathway); confirm that
    # before relying on it for the layout below.
    _validate_adjacent_layer_edges(G, source_col, target_col, edges)

    # ------------------------------------------------------------
    # Custom layout: order nodes within each layer to reduce
    # crossings, then space them out with explicit gaps
    # ------------------------------------------------------------
    layers_sorted = sorted(set(layer_map.values()))
    layer_nodes = {
        layer: [n for n, d in G.nodes(data=True) if d['subset'] == layer]
        for layer in layers_sorted
    }

    order = _order_layers(G, layers_sorted, layer_nodes, sort_by)
    layer_node_gaps = layer_node_gaps or {}

    pos = {}
    for layer in layers_sorted:
        layer_list = order[layer]
        n = len(layer_list)
        gap = layer_node_gaps.get(layer, node_gap)
        ys = np.arange(n) * gap
        ys = ys - ys.mean() if n > 1 else ys
        for y, node in zip(ys, layer_list):
            pos[node] = (layer * layer_gap, y)

    # ------------------------------------------------------------
    # Node sizes (optionally scaled by degree so hubs stand out
    # and leaf nodes shrink out of the way)
    # ------------------------------------------------------------
    degrees = dict(G.degree())
    if node_size_by_degree and degrees:
        max_deg = max(degrees.values()) or 1
        node_sizes = [
            min_node_size + (max_node_size - min_node_size) * (degrees[n] / max_deg)
            for n in G.nodes
        ]
    else:
        node_sizes = min_node_size

    plt.figure(figsize=figsize)

    # Edges
    nx.draw_networkx_edges(
        G, pos,
        alpha=0.12,
        arrows=False,
        width=0.4,
        connectionstyle='arc3,rad=0.05',  # slight curve helps parallel edges separate visually
    )

    # Nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_color=[color_map[G.nodes[n]['node_type']] for n in G.nodes],
        node_size=node_sizes,
        linewidths=0.3,
        edgecolors='white',
    )

    # ------------------------------------------------------------
    # Labels: only label a manageable subset, and avoid overlap
    # ------------------------------------------------------------
    if label_col is not None:
        if label_top_n is not None:
            label_nodes = set()
            for layer in layers_sorted:
                top = sorted(
                    layer_nodes[layer], key=lambda n: degrees[n], reverse=True
                )[:label_top_n]
                label_nodes.update(top)
        elif label_min_degree is not None:
            label_nodes = {n for n in G.nodes if degrees[n] >= label_min_degree}
        else:
            label_nodes = set(G.nodes)

        labels = {n: G.nodes[n]['label'] for n in label_nodes}

        if avoid_label_overlap and HAS_ADJUST_TEXT:
            texts = [
                plt.text(pos[n][0], pos[n][1], label, fontsize=font_size, ha='center', va='center')
                for n, label in labels.items()
            ]
            adjust_text(
                texts,
                arrowprops=dict(arrowstyle='-', color='gray', lw=0.4, alpha=0.6),
            )
        else:
            if avoid_label_overlap and not HAS_ADJUST_TEXT:
                print(
                    "Tip: install 'adjustText' (pip install adjustText) for "
                    "automatic label-overlap avoidance. Falling back to plain labels."
                )
            nx.draw_networkx_labels(
                G, pos, labels=labels, font_size=font_size,
            )

    plt.axis('off')
    plt.tight_layout()
    plt.savefig(save_path, dpi=dpi, bbox_inches='tight')

    return G, pos
