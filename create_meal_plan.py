import random 

def create_meal_plan(recommended_recipes,  user_diet):
    """Creates a meal plan based on the recommended recipes and user preferences."""

    meal_plan = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    nutritional_goals = user_diet.get("nutritional_goals", {}) # {'calories': 1500, 'protein': 75, 'carbs': 50, 'fat': 100}

    def daily_totals_meet_goals(daily_totals):
        for nutrient, goal in nutritional_goals.items():
            if nutrient == "calorie" and goal - 200 <= nutrient: # Allow a 200 calorie margin of error
                continue
            elif daily_totals.get(nutrient, 0) < goal:
                return False
        return True

    def update_daily_totals(daily_totals, recipe_nutrition):
        for nutrient, value in recipe_nutrition.items():
            daily_totals[nutrient] = daily_totals.get(nutrient, 0) + value

    days = list(meal_plan.keys())
    daily_nutrition = []
    
    for day in days:
        daily_totals = {'calories': 0, 'protein': 0, 'carbs': 0, 'fat': 0}  # Track the nutritional totals for the current day

        while not daily_totals_meet_goals(daily_totals) or daily_totals["calories"] < nutritional_goals["calories"]:
            
            recipe = random.choice(recommended_recipes)  # Randomly select a recipe from the recommended list
            recipe_name = list(recipe.keys())[0]  # Get the recipe name

            recipe_nutrition = recipe.get("nutrition")

            meal_plan[day].append(recipe_name)

            update_daily_totals(daily_totals, recipe_nutrition)
            
            if daily_totals["calories"] > nutritional_goals["calories"] + 200:
                break
            
        daily_nutrition.append([day, daily_totals])

    return meal_plan, daily_nutrition

