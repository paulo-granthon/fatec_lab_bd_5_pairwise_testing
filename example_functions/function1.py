"""
Possible combinations for pairwise testing:
- x: [positive even, positive odd, negative even, negative odd]
- y: [positive even, positive odd, negative even, negative odd]

Test all combinations of `x` and `y`.
"""


def function1(x, y):
    """
    Returns a string based on the value of x and y:
    - "Even" if x + y is a positive even number.
    - "Odd" if x + y is a positive odd number.
    - "Negative Even" if x + y is a negative even number.
    - "Negative Odd" if x + y is a negative odd number.
    - A range of integers from 0 to x if x is negative.

    Args:
    x (int): The first number.
    y (int): The second number.

    Returns:
    str: A description of the sum's parity or a range of integers.
    """
    if x + y > 0:
        if (x + y) % 2 == 0:
            return "Even"
        return "Odd"
    for i in range(abs(x)):
        print(i)
    if (x + y) % 2 == 0:
        return "Negative Even"
    return "Negative Odd"
