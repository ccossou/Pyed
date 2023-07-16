from pyed.core import utils
import pytest

test_data = [
    ("t", None),
    (1.0, None),
    (1, None),
    (2, [2, 3, 4]),
    (4, [2, 4]),
]


@pytest.mark.parametrize("val, val_list", test_data)
def test_check_value(val, val_list):
    """
    Test check_value
    """
    utils.check_value("", val, val_list)


test_data = [
    (None, None),
    ([], None),
    ([1, 1], None),
    (-1, [1, 2]),
    ('t', [1, 2]),
]


@pytest.mark.parametrize("val, val_list", test_data)
def test_check_value_fail(val, val_list):
    """
    Test check_value failures
    """
    with pytest.raises(ValueError):
        utils.check_value("", val, val_list)
