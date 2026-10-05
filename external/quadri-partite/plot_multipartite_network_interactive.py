import networkx as nx
import numpy as np
import plotly.graph_objects as go

# Reuses the crossing-reduction layout logic and edge validation from
# the static version.
from plot_multipartite_network import _order_layers, _validate_adjacent_layer_edges


def plot_multipartite_network_interactive(
    edges,
    nodes,
    source_col='source',
    target_col='target',
    node_col='id',
    type_col='type',
    label_col='id',
    layer_gap=3.0,
    node_gap=1.0,
    layer_node_gaps=None,      # optional dict {layer_index: node_gap} for dense layers
    sort_by='barycenter',
    node_size_by_degree=True,
    min_node_size=4,
    max_node_size=18,
    edge_opacity=0.12,
    save_path='lqn.html',
    title='Multipartite network',
    width=1600,
    height=1000,
):
    """
    Same data model as plot_multipartite_network, but renders an
    interactive Plotly figure: labels appear on hover instead of
    being drawn on the canvas, so dense layers (hundreds of nodes)
    stay fully readable without any static layout compromise.
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

    edge_nodes = set(edges[source_col]) | set(edges[target_col])
    missing_nodes = edge_nodes - set(G.nodes)
    if missing_nodes:
        raise ValueError(
            f'{len(missing_nodes)} nodes in edges are missing '
            'from the nodes dataframe.\n'
            f'Examples: {list(missing_nodes)[:10]}'
        )

    G.add_edges_from(
        edges[[source_col, target_col]].itertuples(index=False, name=None)
    )

    # Edges are expected to only ever connect consecutive layers
    # (MicroRNA -> Messenger RNA -> Semantics -> Pathway); confirm that
    # before relying on it for the layout below.
    _validate_adjacent_layer_edges(G, source_col, target_col, edges)

    # ------------------------------------------------------------
    # Layout (same crossing-reduction + per-layer spacing as static)
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

    degrees = dict(G.degree())
    max_deg = max(degrees.values()) or 1

    # ------------------------------------------------------------
    # Edge trace (single Scatter with None-separated segments keeps
    # this fast even with thousands of edges)
    # ------------------------------------------------------------
    edge_x, edge_y = [], []
    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color=f'rgba(120,120,120,{edge_opacity})'),
        hoverinfo='none',
        mode='lines',
        showlegend=False,
    )

    # ------------------------------------------------------------
    # One node trace per layer (so the legend can toggle layers on/off)
    # ------------------------------------------------------------
    node_traces = []
    for node_type, layer in layer_map.items():
        layer_node_ids = layer_nodes[layer]
        if not layer_node_ids:
            continue

        xs = [pos[n][0] for n in layer_node_ids]
        ys = [pos[n][1] for n in layer_node_ids]
        labels = [
            f"{G.nodes[n]['label']}<br>degree: {degrees[n]}"
            for n in layer_node_ids
        ]

        if node_size_by_degree:
            sizes = [
                min_node_size + (max_node_size - min_node_size) * (degrees[n] / max_deg)
                for n in layer_node_ids
            ]
        else:
            sizes = min_node_size

        node_traces.append(go.Scatter(
            x=xs, y=ys,
            mode='markers',
            marker=dict(
                size=sizes,
                color=color_map[node_type],
                line=dict(width=0.5, color='white'),
            ),
            text=labels,
            hovertemplate='%{text}<extra>' + node_type + '</extra>',
            name=node_type,
        ))

    fig = go.Figure(data=[edge_trace, *node_traces])
    fig.update_layout(
        title=title,
        showlegend=True,
        hovermode='closest',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white',
        width=width,
        height=height,
    )

    fig.write_html(save_path)
    return fig
