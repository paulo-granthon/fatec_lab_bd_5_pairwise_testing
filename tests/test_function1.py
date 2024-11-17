import pytest
from example_functions import function1


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, "Odd"),  # positive even + positive odd = odd
    (2, 2, "Even"),  # positive even + positive even = even
    (-2, 2, "Negative Even"),  # negative even + positive even = negative even
    (-3, -3, "Negative Even"),  # negative odd + negative odd = negative even
    (-2, 1, "Negative Odd"),  # negative even + positive odd = negative odd
])
def test_function1(x, y, expected):
    """
    Test function1 for different combinations of x and y values.

    This function tests combinations of positive even, positive odd,
    negative even, and negative odd values for both x and y. It checks
    whether the returned result matches the expected output for each
    combination.
    """
    result = function1(x, y)
    assert result == expected
