"""
Layout > One Click Layout
Node labeling: None (if horizontal is set, it removes label placement)
Routing style: Arc
"""

import pyed

def plot_param(g, model_name, placements):
    parent = g.add_node(pyed.ShapeNode, f"{model_name}", width="60")

    kwargs = {"autoSizePolicy": "content", "lineColor": "#ff0000"}
    for value in placements:
        kwargs["modelName"] = model_name  # To override existing parameter if any
        kwargs["modelPosition"] = value  # To override existing parameter if any

        node = g.add_node(pyed.ShapeNode, f"{value}", height="60", width="80", title_style=kwargs)
        g.add_edge(parent, node)


params = {
    "internal": ["t", "b", "c", "l", "r", "tl", "tr", "bl", "br"],
    "corners": ["nw", "ne", "sw", "se"],
    "sandwich": ["n", "s"],
    "sides": ["n", "e", "s", "w"],
    "eight_pos": ["n", "e", "s", "w", "nw", "ne", "sw", "se"],
    "custom": [None],
    "free": ["anywhere"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"label_placement.graphml"
g.write_graph(out_filename)
