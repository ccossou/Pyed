import pyed

g = pyed.Graph()

n1 = g.add_node(pyed.ShapeNode, 'foo', title_style=dict(fontFamily="Zapfino"))
n2 = g.add_node(pyed.ShapeNode, 'foo2', shape="roundrectangle", title_style=dict(fontStyle="bolditalic",
           underlined_text="true"))

e1 = g.add_edge(n1, n2)
n3 = g.add_node(pyed.UmlNode, "UmlNode", stereotype="abstract", attributes="foo\nbar", methods="foo()\nbar()")

b = g.add_node(pyed.ShapeNode, 'bar')

f = g.add_node(pyed.ShapeNode, 'foobar')

l = g.add_node(pyed.GenericNode, "Entity", description="line1\nline2\nline3")

table = [
    ("Rows", "Name", "Unit"),
    ("Row 0", "toto", "str"),
    ("Row 1", 123, "int"),
]

t = g.add_node(pyed.TableNode, "Entity", table=table)


e2 = g.add_edge(n2, n3, label="EDGE!", width="3.0", color="#0000FF",
                 arrowhead="white_diamond", arrowfoot="standard", line_type="dotted")

grp1 = g.add_group("MY_Group", shape="rectangle3d")
n4 = grp1.add_node(pyed.ShapeNode, 'foo4', shape="roundrectangle", title_style=dict(fontStyle="bolditalic",
            underlinedText="true"))
n5 = grp1.add_node(pyed.ShapeNode, 'abc2', title_style=dict(fontSize="72"), height="100")

g.add_edge(n4, n5)
g.add_edge(n2, grp1)

n6 = g.add_node(pyed.SvgNode, "SvgNode", svg_filename="yed_regular_hexagon.svg")

for (idx, n) in g.nodes.items():
    print(f"{idx}: {n.name}")

for (idx, n) in g.groups.items():
    print(f"{idx}: {n.name}")

g.write_graph("test.graphml")
