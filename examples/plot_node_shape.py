"""
Layout > Radial
Node labeling: None
Routing style: Arc
"""

import pyed

def plot_param(g, param_name, values):
    parent = g.add_node(pyed.ShapeNode, f"{param_name}")

    for value in values:
        kwargs = {param_name: value}

        node = g.add_node(pyed.ShapeNode, f"{value}", **kwargs)
        g.add_edge(parent, node)


params = {
    "shape": ["rectangle", "rectangle3d", "roundrectangle", "diamond", "ellipse",
                   "fatarrow", "fatarrow2", "hexagon", "octagon", "parallelogram",
                   "parallelogram2", "star5", "star6", "star6", "star8", "trapezoid",
                   "trapezoid2", "triangle", "trapezoid2", "triangle"],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"node_shape.graphml"
g.write_graph(out_filename)
