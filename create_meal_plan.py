def create_meal_plan(recommended_recipes, user_diet):
    """Creates a meal plan based on the recommended recipes and user preferences."""
    
    # Initialize a meal plan dictionary with each day of the week
    meal_plan = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }
    
    # Extract the nutritional goals from the user's diet preferences
    nutritional_goals = user_diet.get("nutritional_goals", {})
    
    # Function to check if a recipe meets nutritional goals
    def recipe_meets_goals(recipe):
        for nutrient, goal in nutritional_goals.items():
            if recipe.get("nutrition", {}).get(nutrient, 0) > goal:
                return False
        return True

    # Distribute recipes across the week
    days = list(meal_plan.keys())
    used_recipes = set()  # Track used recipes to avoid repetition
    recipe_index = 0

    for day in days:
        while recipe_index < len(recommended_recipes):
            recipe = recommended_recipes[recipe_index]
            recipe_name = list(recipe.keys())[0]  # Get the recipe name
            
            # Check if the recipe has already been used
            if recipe_name in used_recipes:
                recipe_index += 1
                continue
            
            # Check if the recipe meets the user's nutritional goals
            if recipe_meets_goals(recipe[recipe_name]):
                meal_plan[day] = recipe  # Assign the recipe to the current day
                used_recipes.add(recipe_name)  # Mark the recipe as used
                recipe_index += 1
                break  # Move to the next day
            
            recipe_index += 1

        # If we've gone through all recipes and none are suitable, reset the index
        if recipe_index >= len(recommended_recipes):
            recipe_index = 0

    return meal_plan
