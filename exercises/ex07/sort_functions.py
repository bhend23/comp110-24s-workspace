"""Functions that implement sorting algorithms."""

__author__ = "730664108"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    idx: int = 0
    list_length = len(x)
    while idx < list_length - 1:
        plus = idx + 1
        current = x[plus]
        while plus > 0 and x[plus - 1] > current:
            x[plus], x[plus - 1] = x[plus -1], x[plus]
            plus -= 1
        idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    list_length = len(x)
    counter: int = 0
    while counter < list_length:
        min_index = counter
        y = min_index + 1
        while y < list_length:
            if x[y] < x[min_index]:
                min_index = y
            y += 1
        temp = x[counter]
        x[counter] = x[min_index]
        x[min_index] = temp
        counter += 1
    return None
    