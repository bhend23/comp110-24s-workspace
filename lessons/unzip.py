"""Splitting a dictionary into two lists."""

__author__ = "730664108"


def get_keys(word_number: dict[str, int]) -> list[str]:
    """Returns a list of keys from the given dictionary."""
    list1: list[str] = []
    if word_number == {}:
        return list1
    for key in word_number:
        list1.append(key)
    return list1


def get_values(vald: dict[str, int]) -> list[int]:
    """Produces a list of all the values in the input dictionary."""
    list1: list[int] = []
    if vald == {}:
        return list1
    for key in vald:
        list1.append(vald[key])
    return list1