import pytest
from example_functions import function2


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, "positive product"),  # positive * positive = positive
    (-2, -3, "positive product"),  # negative * negative = positive
    (2, -3, "negative product"),  # positive * negative = negative
    (0, 3, "zero product"),  # zero * positive = zero
    (2, 0, "zero product"),  # positive * zero = zero
])
def test_function2(a, b, expected):
    """
    Test function2 for different combinations of a and b values.

    This function tests combinations of positive, negative, and zero values
    for both a and b. It checks whether the returned result matches the
    expected output based on the sign of their product.
    """
    result = function2(a, b)
    assert result == expected
