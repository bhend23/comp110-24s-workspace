"""Unit tests for dictionary.py!"""

__author__ = "730664108"


from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance


def test_invert_use1() -> None:
    """Function should switch the value and key."""
    a = {"colors": "blue"}
    assert invert(a) == {'blue': 'colors'}


def test_invert_use2() -> None:
    """If there are multiple keys, it should switch each one with their respected values."""
    a: dict[str, str] = {"colors": "blue", "animals": "tiger"}
    assert invert(a) == {'blue': 'colors', 'tiger': 'animals'}


def test_invert_edge() -> None:
    """If the dictionary is empty, should return an empty dictionary."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_favorite_color_use1() -> None:
    """Should return the color that appears most often."""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_color_use2() -> None:
    """If there is only one entry, should return that entry's color."""
    a = {"Marc": "yellow"}
    assert favorite_color(a) == "yellow"


def test_favorite_color_edge() -> None:
    """If there is nothing in the dictionary, should return an empty string."""
    a: dict[str, str] = {}
    assert favorite_color(a) == ""


def test_count_use1() -> None:
    """If there is just one variable int he list multiple times, it will count how many times it appears."""
    a: list[str] = ["blue", "blue",]
    assert count(a) == {'blue': 2}


def test_count_use2() -> None:
    """If there are multiple different variables in the list it will make a dictionary of each variable with the keys being how many times it appears."""
    a: list[str] = ["blue", "blue", "red", "purple", "purple"]
    assert count(a) == {'blue': 2, 'red': 1, 'purple': 2}


def test_count_edge() -> None:
    """If there is nothing in the list, an empty dictionary will be returned."""
    a: list[str] = []
    assert count(a) == {}


def test_alphabetizer_use1() -> None:
    """If there is just one variable in the list, it will make just one dictionary key for that variable."""
    a: list[str] = ["blue"]
    assert alphabetizer(a) == {'b': ['blue']}


def test_alphabetizer_use2() -> None:
    """If there are multiple different variables with different starting letters, will make a seperate dictionary key for each."""
    a: list[str] = ["blue", "bar", "cat", "dog", "unc", "duke", "cart"]
    assert alphabetizer(a) == {'b': ['blue', 'bar'], 'c': ['cat', 'cart'], 'd': ['dog', 'duke'], 'u': ['unc']}


def test_alphabetizer_edge() -> None:
    """If the list is empty, should return an empty dict."""
    a: list[str] = []
    assert alphabetizer(a) == {}


def test_update_attendance_use1() -> None:
    """If you update the log with a key already in the dictionary but a new name, will not make another key but add to the dictionary under the already established key."""
    a = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(a, "Monday", "Brandon")
    assert a == {'Monday': ['Vrinda', 'Kaleb', 'Brandon'], 'Tuesday': ['Alyssa']}


def test_update_attendance_use2() -> None:
    """If the day is not already in the dictionary as a key, will add the day and name."""
    a = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(a, "Wednesday", "Brandon")
    assert a == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['Brandon']}


def test_update_attendance_edge() -> None:
    """If given an empty empty string for 'name' will add the key and an empty string as the value."""
    a = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(a, "Wednesday", "")
    assert a == {'Monday': ['Vrinda', 'Kaleb'], 'Wednesday': [''], 'Tuesday': ['Alyssa']}