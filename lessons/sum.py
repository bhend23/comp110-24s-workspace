"""Sums with different loops."""

__author__ = "730664108"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of a list!"""
    if not vals:
        return 0.0
    idx: int = 0
    total: float = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total
    

def f_sum(vals: list[float]) -> float:
    """Returns sum of a list using for in loop!"""
    total: float = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of each element in a list using range!"""
    total: float = 0.0
    for elem in range(0, len(vals)):
        total += vals[elem]
    return total
