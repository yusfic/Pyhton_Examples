# Define the restaurant options and their dietary restrictions
restaurants = {
    "Joe's Gourmet Burgers": {"Vegetarian": "No", "Vegan": "No", "Gluten-Free": "No"},
    "Main Street Pizza Company": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "Yes"},
    "Corner Cafe": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "Yes"},
    "Mama's Fine Italian": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "No"},
    "The Chef's Kitchen": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "Yes"}
}

# Ask about dietary restrictions
is_vegetarian = input("Is anyone in your party a vegetarian? (yes/no): ").lower()
is_vegan = input("Is anyone in your party a vegan? (yes/no): ").lower()
is_gluten_free = input("Is anyone in your party gluten-free? (yes/no): ").lower()

# Initialize a list to store restaurant choices
valid_restaurants = []

# Check each restaurant for dietary compatibility
for restaurant, restrictions in restaurants.items():
    if (is_vegetarian == "yes" or restrictions["Vegetarian"] == "Yes") and \
       (is_vegan == "yes" or restrictions["Vegan"] == "Yes") and \
       (is_gluten_free == "yes" or restrictions["Gluten-Free"] == "Yes"):
        valid_restaurants.append(restaurant)

# Display the valid restaurant choices
if valid_restaurants:
    print("\nHere are your restaurant choices:")
    for restaurant in valid_restaurants:
        print(restaurant)
else:
    print("\nNo restaurant options available based on dietary restrictions.")








