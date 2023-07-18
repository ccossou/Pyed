"""
Layout > Hierarchical > Left to Right
Layout > Edge routing > Straight Line
"""
import pyed


def plot_param(g, model_name, placements):
    kwargs = {"backgroundColor": "#ffffff", "lineColor": "#ff0000"}
    for value in placements:
        parent = g.add_node(pyed.ShapeNode, f"{model_name}")
        kwargs["modelName"] = model_name  # To override existing parameter if any
        kwargs["modelPosition"] = value  # To override existing parameter if any

        node = g.add_node(pyed.ShapeNode, "target")
        g.add_edge(parent, node, label=f"{value}", label_style=kwargs)


params = {
    "two_pos": ["head", "tail"],
    "centered": ["center"],
    "six_pos": ["shead", "thead", "head", "stail", "ttail", "tail"],
    "three_center": ["center", "scentr", "tcentr"],
    # "center_slider": [None],
    # "side_slider": [None],
    "free": ["anywhere"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"edge_label_placement.graphml"
g.write_graph(out_filename)
