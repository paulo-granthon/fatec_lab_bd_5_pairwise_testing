"""
Possible combinations for pairwise testing:
- n: [prime, non-prime, negative number, 0, 1]

Test all combinations of `n`.
"""


def function4(n):
    """
    Checks if a number is prime:
    - Returns "prime" if the number is prime.
    - Returns "not prime" if the number is not prime.
    - Returns "negative" for negative numbers.
    - Returns "zero or one" for 0 or 1.

    Args:
    n (int): The number to check.

    Returns:
    str: "prime", "not prime", "negative", or "zero or one".
    """
    if n < 0:
        return "negative"
    if n <= 1:
        return "zero or one"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "not prime"

    return "prime"
