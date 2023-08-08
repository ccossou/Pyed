import pyed
import pyed.elements as pel
from pyed import utils


def test_shapenode():
    """
    Test ShapeNode constructor
    """
    g = pyed.Graph()

    n1 = g.add_node(pel.ShapeNode, "foo")

    tlabel = n1.list_of_labels[0]
    assert tlabel._text == "foo"
    assert n1.shape == "rectangle"
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    n2 = g.add_node(pel.ShapeNode, "foo2", shape="rectangle3d", title_style=dict(underlinedText="true",
                                                                         backgroundColor="#df4512"))

    assert n2.shape == "rectangle3d"
    assert n2.parent.id == g.id
    assert n2.parent_graph.id == g.id

    ref_dict["underlinedText"] = "true"
    ref_dict["backgroundColor"] = "#df4512"
    tlabel = n2.list_of_labels[0]
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)
