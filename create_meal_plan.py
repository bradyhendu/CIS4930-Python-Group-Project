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

    # Function to check if the current daily total meets nutritional goals
    def daily_totals_meet_goals(daily_totals):
        for nutrient, goal in nutritional_goals.items():
            if daily_totals.get(nutrient, 0) < goal:
                return False
        return True

    # Function to update daily nutritional totals
    def update_daily_totals(daily_totals, recipe_nutrition):
        for nutrient, value in recipe_nutrition.items():
            daily_totals[nutrient] = daily_totals.get(nutrient, 0) + value

    days = list(meal_plan.keys())
    used_recipes = set()  # Track used recipes to avoid repetition
    recipe_index = 0

    # Iterate over each day to populate meal plan
    for day in days:
        daily_totals = {}  # Track the nutritional totals for the current day

        # Keep adding recipes until the daily nutritional goals are met
        while not daily_totals_meet_goals(daily_totals) and recipe_index < len(recommended_recipes):
            recipe = recommended_recipes[recipe_index]
            recipe_name = list(recipe.keys())[0]  # Get the recipe name

            # Check if the recipe has already been used
            if recipe_name in used_recipes:
                recipe_index += 1
                continue

            # Get the nutritional info of the recipe
            recipe_nutrition = recipe[recipe_name].get("nutrition", {})

            # Add recipe to the meal plan for the current day
            meal_plan[day].append(recipe_name)
            used_recipes.add(recipe_name)  # Mark the recipe as used

            # Update daily nutritional totals
            update_daily_totals(daily_totals, recipe_nutrition)

            # Move to the next recipe
            recipe_index += 1

            # Reset the recipe index if we've exhausted the list
            if recipe_index >= len(recommended_recipes):
                recipe_index = 0

    return meal_plan

