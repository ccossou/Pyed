import pyed

g = pyed.Graph()

n1 = g.add_node(pyed.ShapeNode, 'ShapeNode')

n2 = g.add_node(pyed.GenericNode, "GenericNode", description="line1\nline2\nline3")

n3 = g.add_node(pyed.UmlNode, "UmlNode", stereotype="abstract", attributes="foo\nbar", methods="foo()\nbar()")

e1 = g.add_edge(n1, n2, label="Edge", label_style=dict(backgroundColor="#ffffff"))

table = [
    ("Rows", "Name", "Unit"),
    ("Row 0", "toto", "str"),
    ("Row 1", 123, "int"),
]

t = g.add_node(pyed.TableNode, "TableNode", table=table)

grp1 = g.add_group("Group")
n4 = grp1.add_node(pyed.ShapeNode, "foo")
n5 = grp1.add_node(pyed.ShapeNode, "bar")
e2 = grp1.add_edge(n4, n5)

g.write_graph("nodetypes.graphml")
