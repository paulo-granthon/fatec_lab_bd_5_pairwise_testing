import pytest
from example_functions import function5


@pytest.mark.parametrize("x, y, z, expected", [
    (1, 2, 3, "all positive"),  # all positive
    (-1, -2, -3, "all negative"),  # all negative
    (1, -2, 3, "mixed"),  # mixed signs
    (0, 0, 0, "mixed"),  # mixed signs (zero values)
])
def test_function5(x, y, z, expected):
    """
    Test function5 for different combinations of x, y, and z values.

    This function tests combinations of positive, negative, and zero values
    for x, y, and z. It checks whether the function correctly identifies
    whether all numbers are positive, all negative, or mixed in signs.
    """
    result = function5(x, y, z)
    assert result == expected
