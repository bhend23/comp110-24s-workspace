"""Practice with disctionaries"""

ice_cream: dict[str, int] = {'chocolate': 12, 'vanilla': 8, 'strawberry': 5}

# Adding
ice_cream['mint'] = 3
print("After adding mint:")
print(ice_cream)

# Removing
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

# Accessomg
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# Updating Value
print("After adding one vanilla")
ice_cream["vanilla"] += 1
print(f"Number of vanilla orders: {ice_cream['vanilla']}")

# Checking if in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)