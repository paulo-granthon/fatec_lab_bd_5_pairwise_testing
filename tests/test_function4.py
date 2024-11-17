import pytest
from example_functions import function4


@pytest.mark.parametrize("n, expected", [
    (2, "prime"),  # prime number
    (4, "not prime"),  # non-prime number
    (-3, "negative"),  # negative number
    (0, "zero or one"),  # zero
    (1, "zero or one"),  # one
])
def test_function4(n, expected):
    """
    Test function4 for different numbers, checking primality and special cases.

    This function tests whether a number is prime, negative, or zero/one.
    It checks all relevant combinations of numbers to ensure the function's correctness.
    """
    result = function4(n)
    assert result == expected
