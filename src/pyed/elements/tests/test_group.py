import pyed
import pyed.elements as pel
from pyed import utils
import pytest


def test_group():
    """
    Test Group constructor
    """
    g = pyed.Graph()

    grp1 = g.add_group("MY_Group")

    tlabel = grp1.list_of_labels[0]
    assert tlabel._text == "MY_Group"
    assert grp1.shape == "rectangle"
    assert grp1.parent.id == g.id
    assert grp1.parent_graph.id == g.id

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in grp1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    grp2 = g.add_group("MY_Group", shape="rectangle3d", title_style=dict(underlinedText="true",
                                                                         backgroundColor="#df4512"))

    assert grp2.shape == "rectangle3d"
    assert grp2.parent.id == g.id
    assert grp2.parent_graph.id == g.id

    ref_dict["underlinedText"] = "true"
    ref_dict["backgroundColor"] = "#df4512"
    tlabel = grp2.list_of_labels[0]
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)


def test_group_nodes():
    """
    Test group.add_node
    """
    g = pyed.Graph()

    grp1 = g.add_group("MY_Group", shape="rectangle3d")

    n1 = grp1.add_node(pel.ShapeNode, 'foo')
    label = n1.list_of_labels[0]
    assert label._text == "foo"
    assert n1.shape == "rectangle"
    assert n1.parent.id == grp1.id
    assert n1.parent_graph.id == g.id

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(label._params, ref_dict)

    n2 = grp1.add_node(pyed.ShapeNode, 'foo4', shape="roundrectangle", title_style=dict(fontStyle="bolditalic"))
    label = n2.list_of_labels[0]
    assert label._text == "foo4"
    assert n2.shape == "roundrectangle"
    assert n2.parent.id == grp1.id
    assert n2.parent_graph.id == g.id

    assert grp1.nodes[n1.id] == n1
    assert grp1.nodes[n2.id] == n2

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_title_style.items() if v is not None}
    ref_dict["fontStyle"] = "bolditalic"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(label._params, ref_dict)



def test_group_link_nodes():
    """
    Test group.link_node
    """
    g = pyed.Graph()

    n1 = g.add_node(pel.ShapeNode, 'foo')

    grp1 = g.add_group("MY_Group", shape="rectangle3d")

    grp1.link_node(n1)

    assert n1.parent.id == grp1.id
    assert n1.parent_graph.id == g.id
    assert n1.id in grp1.nodes
    assert n1.id not in g.nodes


def test_group_edges():
    """
    Test group.add_edge
    """
    g = pyed.Graph()

    grp1 = g.add_group("MY_Group", shape="rectangle3d")

    n1 = grp1.add_node(pel.ShapeNode, 'foo')
    n2 = grp1.add_node(pyed.ShapeNode, 'foo2')
    n3 = grp1.add_node(pyed.ShapeNode, 'foo3')

    e1 = grp1.add_edge(n1, n2)

    assert e1.node1.id == n1.id
    assert e1.node2.id == n2.id
    assert e1.parent.id == grp1.id
    assert e1.parent_graph.id == g.id

    e2 = grp1.add_edge(n1, n3)
    assert e2.node1.id == n1.id
    assert e2.node2.id == n3.id
    assert e2.parent.id == grp1.id
    assert e2.parent_graph.id == g.id

    assert grp1.edges[e1.id] == e1
    assert grp1.edges[e2.id] == e2



def test_group_edges_warning():
    """
    Test group.add_edge warnings
    """
    g = pyed.Graph()

    n1 = g.add_node(pel.ShapeNode, 'foo')

    grp1 = g.add_group("MY_Group", shape="rectangle3d")

    n2 = grp1.add_node(pyed.ShapeNode, 'foo2')
    n3 = grp1.add_node(pyed.ShapeNode, 'foo3')

    with pytest.raises(RuntimeWarning):
        grp1.add_edge(n1, n2)


def test_group_groups():
    """
    Test group.add_group
    """
    g = pyed.Graph()

    grp1 = g.add_group("MY_Group", shape="rectangle3d")

    grp2 = grp1.add_group("g2")

    assert grp2.parent.id == grp1.id
    assert grp2.parent_graph.id == g.id

    grp3 = grp1.add_group("g3")
    assert grp3.parent.id == grp1.id
    assert grp3.parent_graph.id == g.id


    assert grp1.groups[grp2.id] == grp2
    assert grp1.groups[grp3.id] == grp3
