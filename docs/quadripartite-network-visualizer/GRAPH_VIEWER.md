# Quadripartite Network Viewer

`graph_viewer.html` is a self-contained HTML/JS page (no Python, no build
step) for exploring the four-layer transcriptomics network — MicroRNA →
Messenger RNA → Pathway Location → Pathway — described by a nodes CSV and an
edges CSV. Open the file directly in a browser; it loads
[vis-network](https://visjs.github.io/vis-network/) from a CDN and does
everything else client-side.

## Loading data

Keep the HTML and a `data/` folder in the same directory:

```text
graph_viewer.html
data/
    basal-like_nodes.csv
    basal-like_edges.csv
    luminal-a_nodes.csv
    luminal-a_edges.csv
    luminal-b_nodes.csv
    luminal-b_edges.csv
    her2-enriched_nodes.csv
    her2-enriched_edges.csv
```

- **Subtype picker**: the **Basal-like / Luminal A / Luminal B /
  HER2-enriched** buttons automatically fetch the corresponding files
  from `data/<subtype>_nodes.csv` and `data/<subtype>_edges.csv`.
  Clicking a subtype switches the graph and clears its selection. On
  startup, Basal-like is loaded unless a subtype is specified with
  `?file=`. The URL parameter is updated when you pick a subtype.
- **Browse**: the "Browse nodes CSV" and "Browse edges CSV" buttons
  continue to accept manually selected files from any folder.
- **Drag & drop**: drop one or both CSVs onto the dropzone. Each is
  classified by its header (`id`+`type` for nodes, `source`+`target`
  for edges). Loading custom files deselects the subtype buttons.
- **URL parameter**: for example, `graph_viewer.html?file=her2-enriched`
  loads `data/her2-enriched_nodes.csv` and
  `data/her2-enriched_edges.csv`.
- **Local serving**: automatic fetching of CSVs requires an HTTP server;
  browsers typically block `fetch()` from a local `file://` page.
  From the HTML directory, run `python3 -m http.server` and open
  `http://localhost:8000/graph_viewer.html`. Direct Browse and drag &
  drop remain available when opening the HTML directly.
- The graph renders when both CSVs are loaded. Warnings report missing
  edge endpoints or edges connecting nonconsecutive layers.

Expected columns: nodes = `id, label, type` (`MicroRNA`, `Messenger RNA`,
`Pathway Location`, `Pathway`); edges = `source, target`. The original
node type `Semantics` is still accepted as an alias for `Pathway Location`.

The updated pipeline may also export a node-level `qvalue` column and
edge-level `mirtarbase`, `correlation`, and `qvalue` columns. These
additional attributes are parsed without changing the display or
highlighting. Pathway Location node IDs may start with `S` (legacy) or
`PL` (updated); no identifier prefix is required.

## Layout

Nodes are arranged in four vertical layers (left → right, in the order
above). Each layer has its own color **and** shape (the same encoding
as the sibling semantic-box project), so the graph still reads in
grayscale or for color-blind viewers:

| Layer | Color | Shape |
|---|---|---|
| MicroRNA | `#EF3B2C` (red) | diamond |
| Messenger RNA | `#6BAED6` (blue) | circle |
| Pathway Location | `#66CC00` (green) | triangle |
| Pathway | `#FF8000` (orange) | square |

 Within each layer, node order is chosen with the same
barycenter heuristic as `plot_multipartite_network_static.py` (a few
forward/backward sweeps that order each layer by the average position
of its neighbors in the adjacent layer), which keeps edge crossings low.

Layers with hundreds of nodes (e.g. Pathway Location) are wrapped into a grid
of sub-columns rather than one very long column — otherwise the whole
graph would render as an unusably thin sliver. Node size scales with
degree (number of connected edges), so hub nodes stand out.

Positions are fixed once computed (no physics simulation), so the
layout is deterministic and stable — it won't drift or jitter as you
interact with it. Nodes can still be dragged manually if you want to
declutter a specific area.

## Zoom & pan

- Mouse wheel / trackpad pinch to zoom, click-drag to pan.
- Sidebar buttons: **+** / **−** to zoom by a fixed step, **Fit** to
  reset the view to the whole graph.

## Collapsing the sidebar

The **&#10094; / &#10095;** button in the top-left corner of the graph area
collapses the sidebar to hand its width back to the graph, and expands
it again — useful once you've set up your layers/highlight/combine
preferences and just want maximum canvas space. The button stays in
the same corner in both states, so it's always reachable to bring the
sidebar back.

## Click-to-trace highlight

Clicking a node **X** traces two directions independently:

- **Precursors (upstream)** — every node reachable by walking backward
  along edges from X: X's direct predecessors (1st hop), their
  predecessors (2nd hop), and so on, up to how many layers precede X.
- **Successors (downstream)** — the mirror image, walking forward: X's
  direct successors (1st hop), their successors (2nd hop), etc.

Because edges only ever connect one layer to the next, these two sets
never overlap, and a node closer to the "start" (MicroRNA) or "end"
(Pathway) of the network simply has a shorter chain in one direction.

**Styling** (see the "Highlight (on click)" legend in the sidebar):

| Element | Look |
|---|---|
| Selected node(s) | layer color/shape, thick black outline |
| Precursor / successor nodes | keep their layer color and shape |
| Traced edges | dark gray (`#404040`), with an arrowhead |
| Everything else | faded to near-transparent |

Precursors and successors aren't colored differently: precursors are
always to the left of the selection and successors to the right, and
the arrowheads show direction.

**Hop distance** is encoded as opacity, so the trace reads as a
gradient fading away from the selection: 1st hop = full color, 2nd hop
= 55% opacity, 3rd hop = 28% opacity. This applies to both nodes and
edges. Faded (unrelated) edges get no arrowhead.

Click empty canvas space, or the **Clear selection** button, to reset.

### Multi-select: Shift+click, per-gap union / intersection

**Shift+click** a node to add it to the current selection (or remove
it, if it's already selected) instead of replacing the selection —
lets you trace several nodes at once. A plain click (no Shift) always
resets the selection to just that one node.

Instead of one global union/intersection switch, there are **three
independent switches** in the View controls panel, one per gap between
adjacent layers:

- MicroRNA &harr; Messenger RNA
- Messenger RNA &harr; Pathway Location
- Pathway Location &harr; Pathway

Tracing proceeds **one layer at a time**, and each gap's switch decides
how that specific step combines whatever is arriving at it (not the
original selection directly):

- **Union** — a node qualifies if it's reachable through this gap from
  *at least one* node on the near side.
- **Intersection** — a node qualifies only if it's reachable through
  this gap from *every* node on the near side.

Because each gap is resolved in sequence, an intersection at one gap
narrows what continues to the next gap — e.g. selecting two Messenger
RNA nodes with "Messenger RNA ↔ Pathway Location" set to Intersection
keeps only the Pathway Location nodes both directly share; a Pathway
node is then only reached if it's downstream of *those shared Pathway
Location nodes*, which is generally stricter than asking whether it's
downstream of the two Messenger RNA nodes by any path at all. Setting
a gap back to Union restores the "any path counts" behavior for that
step.

This also means a gap's mode can matter even with a **single** selected
node, whenever it fans out to more than one neighbor a couple of hops
away — e.g. selecting one MicroRNA node with several Messenger RNA
targets and setting "Messenger RNA ↔ Pathway Location" to Intersection
shows only the Pathway Location nodes common to *all* of that miRNA's
targets.

The **Selection** panel lists each selected node as a removable chip
(× removes it from the selection without needing to find it again on
the canvas), a note listing which gap(s) are currently set to
Intersection (if any), and the combined Precursors / Successors
breakdown: total count and a per-layer count for each direction.

## Labels & tooltips

Labels are drawn to the **right** of each node, with a white halo so
the node's outgoing edges don't cross out the text. (vis-network's
built-in shapes always place labels below the node, so nodes are drawn
by a custom renderer.) By default, only the smaller layers (MicroRNA, Messenger RNA, Pathway)
show labels; Pathway Location (hundreds of nodes) stays unlabeled to
avoid clutter — hover any node to see its full label and degree in a
tooltip regardless.

Pathway Location labels are a `>`-separated
path (e.g. `Signaling by ERBB4 > Nuclear signaling by ERBB4 > CXCL12
gene expression is stimulated by ERBB4s80:ESR1:estrogen [ACTIVATION]`).
The hover tooltip splits these on `>` and stacks each segment on its
own line instead of showing one long run-on string. Other layers'
tooltips just show the label as-is.

The **"Show all labels (incl. Pathway Location)"** checkbox reveals labels on
every node. If there's an active selection while this is checked,
labels are restricted to the highlighted set (the selected node(s)
plus their combined precursors/successors) rather than showing all
~278 labels at once — clear the selection to go back to showing every
label.

## Exporting an image

The **Export image** panel downloads the graph as **SVG** (vector, for
Inkscape/Illustrator or a paper) or **PNG** (the same image rasterized
at 3× for print, scaled down for very large graphs so it stays within
browser canvas limits). The export:

- covers the **whole graph**, not just the part currently visible;
- keeps the current state: node positions (including nodes you dragged),
  the active highlight/fading, and whichever labels are showing;
- uses a white background;
- is named `quadripartite_<subtype>_<YYYYMMDD-HHMM>.svg|png`
  (`custom` instead of the subtype for files you loaded yourself).

## Legend panels

- **Layers**: shape/color + node count per layer.
- **Highlight (on click)**: key for the selected node and traced edges,
  plus the hop-opacity scale described above.
