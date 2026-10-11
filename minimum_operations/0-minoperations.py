#!/usr/bin/python3
"""Module for calculating minimum copy/paste operations to reach n H chars."""


def minOperations(n):
    """Calculate fewest operations to get exactly n H characters.

    Args:
        n (int): target number of H characters.

    Returns:
        int: minimum number of operations, or 0 if impossible.
    """
    if n <= 1:
        return 0
    ops = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1
    return ops
