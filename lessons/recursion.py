"""Recursion practice."""

__author__ = "730664108"


def f(n: int, k: int) -> int:
    """Recursive function."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)