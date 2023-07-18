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
    "arrowhead": ['none', "standard", "white_delta", "diamond", "white_diamond", "short",
               "plain", "concave", "convex", "circle", "transparent_circle", "dash",
               "skewed_dash", "t_shape", "crows_foot_one_mandatory",
               "crows_foot_many_mandatory", "crows_foot_many_optional", "crows_foot_one",
               "crows_foot_many", "crows_foot_optional"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"edge_arrowhead.graphml"
g.write_graph(out_filename)
