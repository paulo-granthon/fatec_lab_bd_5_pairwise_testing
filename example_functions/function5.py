"""
Possible combinations for pairwise testing:
- x: [positive, negative, zero]
- y: [positive, negative, zero]
- z: [positive, negative, zero]

Test all combinations of `x`, `y`, and `z`.
"""


def function5(x, y, z):
    """
    Evaluates whether all three numbers are positive, all negative, or mixed:
    - Returns "all positive" if all numbers are positive.
    - Returns "all negative" if all numbers are negative.
    - Returns "mixed" if the numbers have different signs.

    Args:
    x (int): The first number.
    y (int): The second number.
    z (int): The third number.

    Returns:
    str: "all positive", "all negative", or "mixed".
    """
    if x > 0 and y > 0 and z > 0:
        return "all positive"

    if x < 0 and y < 0 and z < 0:
        return "all negative"

    return "mixed"
