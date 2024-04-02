"""Some functions for my garden plan!"""

__author__ = "730664108"


def add_by_kind(dictionary: dict[str, list[str]], type: str, item: str) -> None:
    """Adds an item or item and type to a dictionary!"""
    if type in dictionary:
        dictionary[type].append(item)
    else:
        dictionary[type] = []
        dictionary[type].append(item)


def add_by_date(garden_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if month in garden_by_date:
        garden_by_date[month].append(plant)
    else:
        garden_by_date[month] = []
        garden_by_date[month].append(plant)


def lookup_by_kind_and_date(garden_by_kind: dict[str, list[str]], garden_by_date: dict[str, list[str]], plant_type: str, month: str) -> str:
    """Searches through both dictionaries and returns string with a list of what plants to plant at certain date."""
    assert plant_type in garden_by_kind
    assert month in garden_by_date
    # Get a list of all plants of the specific kind input.
    kind_list: list[str] = garden_by_kind[plant_type]
    # Get a list of all plants planted in a specific month.
    month_list: list[str] = garden_by_date[month]
    # Go through both lists and find elements that appear in both.
    # kind_list = ["marigold", "daisy"]
    # month list = ["daisy", "rose"]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:
                combined_list.append(plant)
    if len(combined_list) > 0:
        return f"{plant_type} to plant in {month}: {combined_list}"
    else:
        return f"No {plant_type} to plant in {month}."