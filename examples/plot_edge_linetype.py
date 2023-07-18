"""
Layout > Hierarchical (top to bottom)
"""

import pyed

def plot_param(g, param_name, values):
    parent = g.add_node(pyed.ShapeNode, f"{param_name}")

    for value in values:
        kwargs = {param_name: value}

        node = g.add_node(pyed.ShapeNode, f"{value}")
        g.add_edge(parent, node, **kwargs)


params = {
    "line_type": ["line", "dashed", "dotted", "dashed_dotted"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"edge_linetype.graphml"
g.write_graph(out_filename)
