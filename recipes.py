# FILE: recipes.py

recipes = {
    "Pasta": {"ingredients": {"pasta": 100, "tomato": 50}, "diet": "vegetarian"},
    "Chicken Salad": {"ingredients": {"chicken": 150, "lettuce": 50, "onion": 10}, "diet": "non-vegetarian"},
    "Fruit Smoothie": {"ingredients": {"banana": 1, "milk": 200}, "diet": "vegetarian"},
    "Chicken Curry": {"ingredients": {"chicken": 200, "curry powder": 10}, "diet": "non-vegetarian"},
    "Vegetable Stir Fry": {"ingredients": {"carrot": 50, "broccoli": 50}, "diet": "vegetarian"},
    "Beef Stew": {"ingredients": {"beef": 200, "potato": 100}, "diet": "non-vegetarian"},
    "Pancakes": {"ingredients": {"flour": 100, "egg": 1}, "diet": "vegetarian"},
    "Omelette": {"ingredients": {"egg": 2, "cheese": 20}, "diet": "vegetarian"},
    "Rice and Beans": {"ingredients": {"rice": 100, "beans": 100}, "diet": "vegetarian"},
    "Tuna Sandwich": {"ingredients": {"tuna": 100, "bread": 50}, "diet": "non-vegetarian"},
    "Grilled Cheese": {"ingredients": {"bread": 50, "cheese": 20}, "diet": "vegetarian"},
    "Spaghetti Bolognese": {"ingredients": {"pasta": 100, "beef": 100}, "diet": "non-vegetarian"},
}

"""
Recommend recipes based on available ingredients and user preferences.

Args:
    available_ingredients (list of dict): A list of dictionaries where each dictionary represents an ingredient with a "name" key.
    user_preferences (list of dict): A list of dictionaries where each dictionary represents a user preference with a "diet" key.

Returns:
    list of dict: A list of recommended recipes. Each recipe is represented as a dictionary with the recipe name as the key and its details as the value.

The function works as follows:
    1. Extracts the names of available ingredients into a set.
    2. Extracts the diet preferences of the user into a set.
    3. Iterates over each recipe and its details in the `recipes` dictionary.
    4. Counts the number of matching ingredients between the recipe and available ingredients.
    5. If the number of matching ingredients is at least half of the total ingredients in the recipe and the recipe's diet matches the user's diet preferences, the recipe is added to the recommended list.
"""
def recommend_recipes(available_ingredients, user_preferences):
    recommended = []
    available_ingredient_names = {ingredient["name"] for ingredient in available_ingredients}
    user_preferences_diet = {preference["diet"] for preference in user_preferences}
    for recipe, details in recipes.items():
        matching_ingredients = sum(1 for ingredient in details["ingredients"] if ingredient in available_ingredient_names)
        if matching_ingredients >= len(details["ingredients"]) / 2:
            if details["diet"] in user_preferences_diet:
                recommended.append({recipe: details})
    return recommended