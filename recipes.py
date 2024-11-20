# FILE: recipes.py

recipes = {
    "Pasta": {"ingredients": {"pasta": 100, "tomato": 50}, "diet": "vegetarian"},
    "Chicken Salad": {"ingredients": {"chicken": 150, "lettuce": 50, "onion": 10}, "diet": "regular"},
    "Fruit Smoothie": {"ingredients": {"banana": 1, "milk": 200}, "diet": "vegetarian"},
    "Chicken Curry": {"ingredients": {"chicken": 200, "curry powder": 10}, "diet": "regular"},
    "Vegetable Stir Fry": {"ingredients": {"carrot": 50, "broccoli": 50}, "diet": "vegetarian"},
    "Beef Stew": {"ingredients": {"beef": 200, "potato": 100}, "diet": "regular"},
    "Pancakes": {"ingredients": {"flour": 100, "egg": 1}, "diet": "vegetarian"},
    "Omelette": {"ingredients": {"egg": 2, "cheese": 20}, "diet": "vegetarian"},
    "Rice and Beans": {"ingredients": {"rice": 100, "beans": 100}, "diet": "vegetarian"},
    "Tuna Sandwich": {"ingredients": {"tuna": 100, "bread": 50}, "diet": "regular"},
    "Grilled Cheese": {"ingredients": {"bread": 50, "cheese": 20}, "diet": "vegetarian"},
    "Spaghetti Bolognese": {"ingredients": {"pasta": 100, "beef": 100}, "diet": "regular"},
    "Keto Chicken": {"ingredients": {"chicken": 200, "olive oil": 20, "spinach": 50}, "diet": "keto"},
    "Keto Salad": {"ingredients": {"lettuce": 100, "avocado": 50, "olive oil": 20}, "diet": "keto"},
    "Vegan Tacos": {"ingredients": {"tortilla": 2, "black beans": 100, "avocado": 50}, "diet": "vegan"},
    "Vegan Curry": {"ingredients": {"chickpeas": 150, "coconut milk": 100, "spinach": 50}, "diet": "vegan"},
    "Keto Avocado Smoothie": {"ingredients": {"avocado": 1, "spinach": 50, "almond milk": 200}, "diet": "keto"},
    "Keto Beef Stir Fry": {"ingredients": {"beef": 200, "broccoli": 100, "soy sauce": 20}, "diet": "keto"},
    "Vegan Buddha Bowl": {"ingredients": {"quinoa": 100, "chickpeas": 100, "avocado": 50, "spinach": 50}, "diet": "vegan"},
    "Vegan Lentil Soup": {"ingredients": {"lentils": 150, "carrot": 50, "celery": 50, "tomato": 100}, "diet": "vegan"},
    "Vegetarian Super Smoothie": {"ingredients": {"kale": 50, "banana": 1, "chia seeds": 10, "almond milk": 200}, "diet": "vegetarian"},
}

recipe_nutrition = {
    "Pasta": {"calories": 800, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Chicken Salad": {"calories": 850, "protein": 45, "carbs": 40, "fat": 35, "fiber": 25},
    "Fruit Smoothie": {"calories": 850, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Chicken Curry": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegetable Stir Fry": {"calories": 850, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Beef Stew": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Pancakes": {"calories": 850, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Omelette": {"calories": 850, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Rice and Beans": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Tuna Sandwich": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Grilled Cheese": {"calories": 850, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Spaghetti Bolognese": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Keto Chicken": {"calories": 800, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Keto Salad": {"calories": 800, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegan Tacos": {"calories": 900, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegan Curry": {"calories": 900, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Keto Avocado Smoothie": {"calories": 725, "protein": 40, "carbs": 120, "fat": 35, "fiber": 25},
    "Keto Beef Stir Fry": {"calories": 815, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegan Buddha Bowl": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegan Lentil Soup": {"calories": 800, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
    "Vegetarian Super Smoothie": {"calories": 250, "protein": 45, "carbs": 120, "fat": 35, "fiber": 25},
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
    for recipe, details in recipes.items():
        matching_ingredients = sum(1 for ingredient in details["ingredients"] if ingredient in available_ingredient_names)
        if matching_ingredients >= len(details["ingredients"]) / 2:
            if details["diet"] == user_preferences["diet"] or user_preferences["diet"] == "regular":
                recommended.append({recipe: details, "nutrition": recipe_nutrition[recipe]})

    return recommended