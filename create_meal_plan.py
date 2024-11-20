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
            if nutrient == "calories":
                if daily_totals.get(nutrient, 0) < goal - 200 or daily_totals.get(nutrient, 0) > goal + 200:
                    return False
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
        #While not an ideal solution, theoretically, 
        #the loop should break after a certain number of iterations if there is no recipe that meets the nutritional goals
        iteration = 0
        iteration_limit = 1000
        
        
        while not daily_totals_meet_goals(daily_totals) and iteration < iteration_limit:          
            recipe = random.choice(recommended_recipes)  # Randomly select a recipe from the recommended list
            recipe_name = list(recipe.keys())[0]  # Get the recipe name

            recipe_nutrition = recipe.get("nutrition")
            
            update_daily_totals(daily_totals, recipe_nutrition)
            
            # If the daily totals exceed the nutritional goals by more than 200 calories, skip the current recipe
            if daily_totals["calories"] > nutritional_goals["calories"] + 200:
                #remove the recipe from the daily totals
                for nutrient, value in recipe_nutrition.items():
                    daily_totals[nutrient] -= value
                    
                if daily_totals["calories"] < nutritional_goals["calories"] - 200:
                    iteration += 1
                    continue
                else:
                    break
            
            meal_plan[day].append(recipe_name)  # Add the recipe to the current day's meal plan
            iteration += 1

        if iteration == iteration_limit:
            return None, None
        
        daily_nutrition.append([day, daily_totals])

    return meal_plan, daily_nutrition

