import pyed
import pyed.elements as pel
from pyed import utils
import pytest


def test_tablenode():
    """
    Test TableNode constructor
    """
    g = pyed.Graph()

    ref_table = [
        ("Rows", "Name", "Unit"),
        ("Row 0", "toto", "str"),
        ("Row 1", 123, "int"),
        ]

    n1 = g.add_node(pel.TableNode, "foo", table=ref_table)

    tlabel = n1.list_of_labels[0]
    assert tlabel._text == "foo"
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id
    assert n1.table == ref_table

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    tab_label = n1.description_label
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_table_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tab_label._params, ref_dict)

    n2 = g.add_node(pel.TableNode, "foo", table=[], title_style=dict(fontStyle="bold"), table_style=dict(fontSize="20"))

    tlabel = n2.list_of_labels[0]

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_title_style.items() if v is not None}
    ref_dict["fontStyle"] = "bold"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    tab_label = n2.description_label

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n2.default_table_style.items() if v is not None}
    ref_dict["fontSize"] = "20"
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tab_label._params, ref_dict)


def test_tablenode_fail():
    """
    Test TableNode expected failures
    """
    g = pyed.Graph()

    ref_table = [
        ("Rows", "Name"),
        ("Row 0", "toto", "str"),
        ("Row 1", 123, "int"),
    ]

    with pytest.raises(ValueError):
        g.add_node(pel.TableNode, "foo", table=ref_table)

    ref_table = 3
    with pytest.raises(TypeError):
        g.add_node(pel.TableNode, "foo", table=ref_table)
