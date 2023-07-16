import pyed
import pyed.elements as pel
from pyed import utils


def test_genericnode():
    """
    Test GenericNode constructor
    """
    g = pyed.Graph()

    ref_description = "toto\ntata"

    n1 = g.add_node(pel.GenericNode, "foo", description=ref_description)

    tlabel = n1.list_of_labels[0]
    assert tlabel._text == "foo"
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id
    assert n1.description_label._text == ref_description

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    desc_label = n1.description_label
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id
    assert n1.background == "#e8eef7"

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_desc_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(desc_label._params, ref_dict)

    n2 = g.add_node(pel.GenericNode, "foo", description="",
                    background="#ffffff", title_style=dict(fontStyle="bold"), desc_style=dict(fontSize="20"))

    tlabel = n2.list_of_labels[0]
    assert n2.background == "#ffffff"

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_title_style.items() if v is not None}
    ref_dict["fontStyle"] = "bold"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    desc_label = n2.description_label
    assert desc_label._text == ""

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_desc_style.items() if v is not None}
    ref_dict["fontSize"] = "20"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(desc_label._params, ref_dict)
