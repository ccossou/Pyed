"""
Layout > Radial
Node labeling: horizontal
Routing style: Arc
"""

import pyed

def plot_param(g, param_name, values):
    parent = g.add_node(pyed.ShapeNode, f"{param_name}", width="100")

    for value in values:
        kwargs = {"lineColor":"#ff0000"}
        kwargs[param_name] = value  # To override existing parameter if any

        node = g.add_node(pyed.ShapeNode, f"{value}", height="60", width="100",
                          title_style=kwargs)
        g.add_edge(parent, node)


params = {
    "autoSizePolicy": ["node_width", "node_size", "node_height", "content"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"label_size.graphml"
g.write_graph(out_filename)
