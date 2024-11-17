"""
Possible combinations for pairwise testing:
- a: [positive, negative, zero]
- b: [positive, negative, zero]

Test all combinations of `a` and `b`.
"""


def function2(a, b):
    """
    Performs different operations based on the values of a and b:
    - Returns "positive product" if both numbers are positive or both negative.
    - Returns "negative product" if one is negative and the other is positive.
    - Returns "zero product" if one or both numbers are zero.

    Args:
    a (int): The first number.
    b (int): The second number.

    Returns:
    str: A description of the product's sign.
    """
    result = a * b
    if result > 0:
        return "positive product"
    if result < 0:
        return "negative product"
    return "zero product"
