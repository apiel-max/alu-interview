#!/usr/bin/python3
"""Module to calculate rainwater retained between walls."""


def rain(walls):
    """Calculate total rainwater retained between walls.

    Args:
        walls: list of non-negative integers representing wall heights.

    Returns:
        Integer total amount of rainwater retained.
    """
    if not walls:
        return 0

    n = len(walls)
    total = 0

    for i in range(n):
        left_max = max(walls[:i + 1])
        right_max = max(walls[i:])
        total += min(left_max, right_max) - walls[i]

    return total
