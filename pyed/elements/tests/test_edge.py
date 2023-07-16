import pyed
import pyed.elements as pel
from pyed import utils


def test_edges():
    g = pyed.Graph()
    nodea = g.add_node(pel.ShapeNode, 'a')
    nodeb = g.add_node(pel.ShapeNode, 'b')
    nodec = g.add_node(pel.ShapeNode, 'c')

    edge1 = g.add_edge(nodea, nodeb)
    assert pel.Edge._class_counter == 1

    edge2 = g.add_edge(nodea, nodec)
    assert pel.Edge._class_counter == 2

    e1 = g.edges[edge1.id]
    e2 = g.edges[edge2.id]

    assert g.nodes[e1.node1.id].list_of_labels[0]._text == "a"
    assert g.nodes[e1.node2.id].list_of_labels[0]._text == "b"

    assert g.nodes[e2.node1.id].list_of_labels[0]._text == "a"
    assert g.nodes[e2.node2.id].list_of_labels[0]._text == "c"


def test_edge_label():
    g = pyed.Graph()
    nodea = g.add_node(pel.ShapeNode, 'a')
    nodeb = g.add_node(pel.ShapeNode, 'b')

    edge1 = g.add_edge(nodea, nodeb, label="middle", source_label="source", target_label="target")

    clabel = edge1.list_of_labels[0]
    assert clabel._text == "middle"
    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in edge1.default_clabel_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(clabel._params, ref_dict)

    slabel = edge1.list_of_labels[1]
    assert slabel._text == "source"
    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in edge1.default_slabel_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(slabel._params, ref_dict)

    tlabel = edge1.list_of_labels[2]
    assert tlabel._text == "target"
    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in edge1.default_tlabel_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)
