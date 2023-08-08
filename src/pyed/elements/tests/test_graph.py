import pyed
import pyed.elements as pel
from pyed import utils


def test_graph():
    """
    Test Graph constructor
    """
    g = pyed.Graph()

    assert g.directed == "directed"
    # can't test id value as the number is not necessarily one depending on the order or unitest execution.
    # Testing type instead
    assert isinstance(g.id, str)
    assert g.parent == None
    assert g.parent_graph == g

    g2 = pyed.Graph()

    assert g.id != g2.id


def test_graph_nodes():
    """
    Test Graph.add_node
    """
    g = pyed.Graph()
    assert len(g.existing_entities) == 1

    n1 = g.add_node(pel.ShapeNode, 'foo')
    label = n1.list_of_labels[0]
    assert label._text == "foo"
    assert n1.shape == "rectangle"
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id
    assert len(g.existing_entities) == 2

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(label._params, ref_dict)

    n2 = g.add_node(pyed.ShapeNode, 'foo4', shape="roundrectangle", title_style=dict(fontStyle="bolditalic"))
    label = n2.list_of_labels[0]
    assert label._text == "foo4"
    assert n2.shape == "roundrectangle"
    assert n2.parent.id == g.id
    assert n2.parent_graph.id == g.id
    assert len(g.existing_entities) == 3

    assert g.nodes[n1.id] == n1
    assert g.nodes[n2.id] == n2

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_title_style.items() if v is not None}
    ref_dict["fontStyle"] = "bolditalic"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(label._params, ref_dict)


def test_graph_edges():
    """
    Test Graph.add_edge
    """
    g = pyed.Graph()

    n1 = g.add_node(pel.ShapeNode, 'foo')
    n2 = g.add_node(pyed.ShapeNode, 'foo2')
    n3 = g.add_node(pyed.ShapeNode, 'foo3')
    assert len(g.existing_entities) == 4

    e1 = g.add_edge(n1, n2)
    assert len(g.existing_entities) == 5

    assert e1.node1.id == n1.id
    assert e1.node2.id == n2.id
    assert e1.parent.id == g.id
    assert e1.parent_graph.id == g.id

    e2 = g.add_edge(n1, n3, label="toto")
    assert len(g.existing_entities) == 6
    assert e2.node1.id == n1.id
    assert e2.node2.id == n3.id
    assert e2.parent.id == g.id
    assert e2.parent_graph.id == g.id
    assert e2.list_of_labels[0]._text == "toto"

    assert g.edges[e1.id] == e1
    assert g.edges[e2.id] == e2


def test_graph_groups():
    """
    Test Graph.add_group
    """
    g = pyed.Graph()

    grp2 = g.add_group("g2")
    assert len(g.existing_entities) == 2

    assert grp2.parent.id == g.id
    assert grp2.parent_graph.id == g.id

    grp3 = g.add_group("g3", shape="rectangle3d")
    assert len(g.existing_entities) == 3
    assert grp3.parent.id == g.id
    assert grp3.parent_graph.id == g.id
    assert grp3.shape == "rectangle3d"

    assert g.groups[grp2.id] == grp2
    assert g.groups[grp3.id] == grp3
