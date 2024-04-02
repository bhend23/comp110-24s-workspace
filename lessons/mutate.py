"""Mutating functions."""

__author__ = "730664108"


def manual_append(alist: list[int], num: int) -> None:
    """Adds a certain number to the list"""
    alist.append(num)


def double(clist: list[int]) -> None:
    """Doubles each seperate number in the list"""
    index = 0
    while index <len(clist):
        clist[index] *= 2
        index += 1
