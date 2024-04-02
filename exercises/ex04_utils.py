"""Exercise 4, Utils."""

__author__ = "730664108"


def all(list: list[int], number: int) -> bool:
    """Checks if each element in the list is the same."""
    if not list:
        return False
    idx = 0
    while idx < len(list):
        if list[idx] != number:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Max function tells you which number is the largest in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    max_value = input[0]
    idx = 1
    while idx < len(input):
        if input[idx] > max_value:
            max_value = input[idx]
        idx += 1
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """is_equal function checks if two lists are the same."""
    if len(list_1) != len(list_2):
        return False
    idx = 0
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds the elements of list 2 to the existing list 1."""
    idx = 0
    while idx < len(list_2):
        if len(list_2) != 0:
            list_1.append(list_2[idx])
        idx += 1