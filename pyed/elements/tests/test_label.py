import pyed.elements as pel
import pytest


def test_label():
    """
    Test Label
    """
    label = pel.Label("foo", "y:NodeLabel")

    assert label._text == "foo"
    assert label.tag == "y:NodeLabel"
    assert "backgroundColor" not in label._params
    assert "lineColor" not in label._params
    assert "autoSizePolicy" not in label._params

    label = pel.Label("foo", "y:NodeLabel", backgroundColor="#ffffff", lineColor="#000000", autoSizePolicy="content")
    assert label._params["backgroundColor"] == "#ffffff"
    assert label._params["lineColor"] == "#000000"
    assert label._params["autoSizePolicy"] == "content"


def test_label_fails():
    """
    Test Label failures
    """
    with pytest.raises(ValueError):
        pel.Label("foo", "y:bla")

    with pytest.raises(ValueError):
        pel.Label("foo", "y:EdgeLabel", autoSizePolicy="content")

    with pytest.raises(ValueError):
        pel.Label("foo", "y:NodeLabel", visible="toto")


test_data = [
    ("fontStyle", "plain"),
    ("fontStyle", "bold"),
    ("fontStyle", "italic"),
    ("fontStyle", "bolditalic"),
    ("alignment", 'left'),
    ("alignment", 'center'),
    ("alignment", 'right'),
    ("autoSizePolicy", "node_width"),
    ("autoSizePolicy", "node_size"),
    ("autoSizePolicy", "node_height"),
    ("autoSizePolicy", "content"),
    ("visible", "true"),
    ("visible", "false"),
    ("underlinedText", "true"),
    ("underlinedText", "false"),
]


@pytest.mark.parametrize("key, value", test_data)
def test_label_valid_parameters(key, value):
    kwargs = {key: value}
    pel.Label("", "y:NodeLabel", **kwargs)



test_data = [
    ("fontStyle", "toto"),
    ("alignment", 'toto'),
    ("autoSizePolicy", "toto"),
    ("visible", "toto"),
    ("underlinedText", "toto"),
]


@pytest.mark.parametrize("key, value", test_data)
def test_label_invalid_parameters(key, value):
    kwargs = {key: value}
    with pytest.raises(ValueError):
        pel.Label("", "y:NodeLabel", **kwargs)