"""For loops with dictionaries"""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    if in_stock[key]: # in_stock[key] is True
        print(key)