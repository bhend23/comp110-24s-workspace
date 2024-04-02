"""Test my garden functions."""


__author__ = "730664108"


from lessons.garden.garden_helpers import add_by_kind, lookup_by_kind_and_date, add_by_date


def test_add_by_kind_edge() -> None:
    """If function is empty should return same list."""
    dict = {}
    add_by_kind(dict, "apple", "fruit")
    assert dict == {"flower": ["daisy"]}
    

def test_add_by_kind_use() -> None:
    """Add kind to a type."""
    dict = {"flower": ["marigold", "zinnia"], "vegetable": ["carrot"]}
    add_by_kind(dict, "vegetable", "potato")


def test_add_by_date_use_case():
    """Add a new plant to existing month."""
    by_date: dict[str, list[str]] = {"january": ["marigold", "zinnia"], "march": ["carrots"]}
    add_by_date(by_date, "january", "pumpkins")
    assert by_date == {"january": ["marigold", "zinnia", "pumpkins"], "march": ["carrots"]}


def test_add_by_date_edge_case():
    """If given empty dict, should return nothing."""
    by_date: dict = {}
    add_by_date(by_date, "january", "marigold")
    assert by_date == {"january": ["marigold"]}


def test_lookup_by_kind_and_date_use_case():
    """If there is a matching plant, should return a string saying when to plant the plant."""
    by_date: dict[str, list[str]] = {"january": ["marigold", "zinnia"], "march": ["carrots"]}
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    r = lookup_by_kind_and_date(by_kind, by_date, "zinnia", "january")
    assert r == "flower to plant in january: ['zinnia']"


def test_lookup_by_kind_and_date_edge():
    """If nothing is in either dictionary, there should be nothing returned."""
    by_date = {"June": ["marigold"], "February": ["carrots"]}
    by_kind = {"flower": ["zinnia", "marigold"], "vegetable": ["carrots"]}
    x = lookup_by_kind_and_date(by_kind, by_date, "flower", "February")
    assert x == "No flower to plant in February."