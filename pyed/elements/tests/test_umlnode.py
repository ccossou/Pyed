import pyed
import pyed.elements as pel
from pyed import utils


def test_umlnode():
    """
    Test UmlNode constructor
    """
    g = pyed.Graph()

    n1 = g.add_node(pel.UmlNode, "foo")

    tlabel = n1.list_of_labels[0]
    assert tlabel._text == "foo"
    assert n1.stereotype == ""
    assert n1.attributes == ""
    assert n1.methods == ""
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id

    # Filter None values as they are not stored in Label
    ref_dict = {k: v for k, v in n1.default_title_style.items() if v is not None}
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)

    ref_stereotype = "AbstractClass"
    ref_attributes = "toto\ntata"
    ref_methods = "str()\nmethod()"

    n2 = g.add_node(pel.UmlNode, "foo2", stereotype=ref_stereotype, attributes=ref_attributes, methods=ref_methods,
                    title_style=dict(underlinedText="true", backgroundColor="#df4512"))

    assert n2.parent.id == g.id
    assert n2.parent_graph.id == g.id
    assert n2.stereotype == ref_stereotype
    assert n2.attributes == ref_attributes
    assert n2.methods == ref_methods

    ref_dict["underlinedText"] = "true"
    ref_dict["backgroundColor"] = "#df4512"
    tlabel = n2.list_of_labels[0]
    # Test if input param dict is a subset of final dict (as default value in Lable could exist on top of input)
    utils.assert_dict_subset(tlabel._params, ref_dict)
