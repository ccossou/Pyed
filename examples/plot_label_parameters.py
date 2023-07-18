"""
Layout > Radial
Node labeling: horizontal
Routing style: Arc
"""

import pyed

def plot_param(g, param_name, values):
    parent = g.add_node(pyed.ShapeNode, f"{param_name}", width="100")
    kwargs = {}
    if param_name == "alignment":
        kwargs["lineColor"] = "#ff0000"
        kwargs["autoSizePolicy"] = "node_size"

    for value in values:
        kwargs[param_name] = value
        node = g.add_node(pyed.ShapeNode, f"{value}", width="60", title_style=kwargs)
        g.add_edge(parent, node)


params = {
"alignment": ['left', 'center', 'right'],
"fontStyle": ["plain", "bold", "italic", "bolditalic"],
"underlinedText": ["true", "false"],
"lineColor": [None, '#000000', '#FF0000'],
"backgroundColor": [None, '#00FF00', '#FF0000'],
"textColor": ['None', '#00FF00', '#FF0000'],
"fontFamily": ['Dialog', 'Courier'],
"rotationAngle": ['0', '30', '60', '90'],
"fontSize": ['12', '20', '30'],
}

g = pyed.Graph()

for name, values in params.items():
    plot_param(g, name, values)

out_filename = f"label_parameters.graphml"
g.write_graph(out_filename)
