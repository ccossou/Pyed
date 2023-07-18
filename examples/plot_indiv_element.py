import pyed

g = pyed.Graph()
n1 = g.add_node(pyed.ShapeNode, 'ShapeNode')
g.write_graph("shape_node.graphml")

g = pyed.Graph()
n2 = g.add_node(pyed.GenericNode, "GenericNode", description="line1\nline2\nline3")
g.write_graph("generic_node.graphml")

g = pyed.Graph()
n3 = g.add_node(pyed.UmlNode, "UmlNode", stereotype="abstract", attributes="foo\nbar", methods="foo()\nbar()")
g.write_graph("uml_node.graphml")

g = pyed.Graph()
n1 = g.add_node(pyed.ShapeNode, 'node1 (source)')
n2 = g.add_node(pyed.ShapeNode, 'node2 (target)')
e1 = g.add_edge(n1, n2, label="Edge", label_style={"backgroundColor": "#ffffff"})
g.write_graph("edge.graphml")

g = pyed.Graph()
table = [
    ("Rows", "Name", "Unit"),
    ("Row 0", "toto", "str"),
    ("Row 1", 123, "int"),
]

t = g.add_node(pyed.TableNode, "TableNode", table=table)
g.write_graph("table_node.graphml")

g = pyed.Graph()
grp1 = g.add_group("Group")
n4 = grp1.add_node(pyed.ShapeNode, "foo")
n5 = grp1.add_node(pyed.ShapeNode, "bar")
e2 = grp1.add_edge(n4, n5)
g.write_graph("group.graphml")
