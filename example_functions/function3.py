"""
Possible combinations for pairwise testing:
- s: [short string, long string]
- t: [short string, long string]

Test all combinations of `s` and `t`.
"""


def function3(s, t):
    """
    Returns a string based on the length comparison between two strings:
    - "same length" if the strings have the same length.
    - "different length" if the strings have different lengths.

    Args:
    s (str): The first string.
    t (str): The second string.

    Returns:
    str: A description based on the length of the strings.
    """
    if len(s) == len(t):
        return "same length"

    return "different length"
