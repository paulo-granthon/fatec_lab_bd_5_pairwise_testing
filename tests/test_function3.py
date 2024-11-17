import pytest
from example_functions import function3


@pytest.mark.parametrize("s, t, expected", [
    ("abc", "def", "same length"),  # same length
    ("abc", "abcdef", "different length"),  # different length
    ("", "", "same length"),  # same length (both empty)
    ("longer", "short", "different length"),  # different length
])
def test_function3(s, t, expected):
    """
    Test function3 for different combinations of string lengths.

    This function tests different combinations of string lengths for s and t,
    ensuring the result matches whether the lengths of the two strings are
    the same or different.
    """
    result = function3(s, t)
    assert result == expected
