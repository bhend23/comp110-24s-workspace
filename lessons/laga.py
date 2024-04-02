"""Dictionary exercise, EX05."""

__author__ = "730664108"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Changes the keys to values and values to keys!"""
    invert_dict: dict = {}
    for key in dict1:
        value = dict1[key]
        if value in invert_dict:
            raise KeyError("Duplicate error found when trying to invert!")
        invert_dict[value] = key
    return invert_dict


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns which color appears the most frequently."""
    max = 0
    popular: str = None
    color_count: dict = {}
    for names in names_colors:
        color = names_colors[names]
        if color in color_count:
            color_count[color] +=1
        else:
            color_count[color] = 1
        if color_count[color] > max:
            max = color_count[color]
            popular = color
    return popular


def count(list1: list[str]) -> dict[str, int]:
    """Counts each time a variable was in a list."""
    empty_dict: dict = {}
    for elem in list1:
        if elem in empty_dict:
            empty_dict[elem] += 1
        else:
            empty_dict[elem] = 1
    return empty_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of words with that letter."""
    empty_dict: dict = {}
    for word in list1:
        first = list1[0].lower()
        if first not in empty_dict:
            empty_dict[first] = []
        empty_dict[first].append(word)
    return empty_dict


def update_attendance(attendance_list: dict[str, list[str]], day: str, student: str) -> None:
    """Updates a list of attendance with new names."""
    if day not in attendance_list:
        attendance_list[day] = []
    attendance_list[day].append(student)