import pyed
import pyed.elements as pel
import importlib.resources



def test_svgnode():
    """
    Test SvgNode constructor
    """
    g = pyed.Graph()

    svg_filename = importlib.resources.files('pyed.elements.tests') / "custom_node_shape.svg"

    n1 = g.add_node(pel.SvgNode, "foo", svg_filename=svg_filename)

    tlabel = n1.list_of_labels[0]
    assert tlabel._text == "foo"
    assert n1.parent.id == g.id
    assert n1.parent_graph.id == g.id

    with open(svg_filename, 'r') as obj:
        ref_content = obj.read()

    ref_hash = hash(ref_content)

    res = g.resources[n1.res_id]
    assert res.hash == ref_hash
    assert res.resource == ref_content
