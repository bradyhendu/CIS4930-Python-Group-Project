from input import read_ingredients, read_preferences
from recipes import recommend_recipes
from write_output import write_output
from visualize import visualize_nutrition
from create_meal_plan import create_meal_plan
import sys

#outside imports
#import matplotlib.pyplot as plt

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


def create_shopping_list(recommended_recipes, available_ingredients):
    #Loop through the recommended recipes and create a shopping list based on the missing ingredients
    available_ingredient_names = {ingredient["name"] for ingredient in available_ingredients}
    shopping_list = []
    for recipe in recommended_recipes:
        for recipe_name, recipe_details in recipe.items():
            for ingredient, quantity in recipe_details["ingredients"].items():
                if ingredient not in available_ingredient_names:
                    shopping_list.append({"ingredient": ingredient, "quantity": quantity})
                if ingredient in available_ingredient_names:
                    #If the ingredient is available, check if the quantity is sufficient
                    available_quantity = int(next((item["quantity"] for item in available_ingredients if item["name"] == ingredient), 0))
                    if available_quantity < quantity:
                        shopping_list.append({"ingredient": ingredient, "quantity": quantity - available_quantity})
                    #if the ingredient is already in the shopping list, update the quantity
                    for item in shopping_list:
                        if item["ingredient"] == ingredient:
                            item["quantity"] += quantity
    return shopping_list


if __name__ == '__main__':
    
    # Read the ingredients and preferences from the input files
    ingredient_list = read_ingredients("ingredients.csv")
    preference_list = read_preferences("preferences.json")
    
    print("Please review the dietary options below and select the one that best fits your goals:\n")
    for i, preference in enumerate(preference_list, start=1):
        print(f"{i}. {preference['diet']} Diet:")
        for key, value in preference['nutritional_goals'].items():
            print(f"   - {key}: {value} g")
        print()

    choice = input("Enter the number corresponding to your preferred diet (1 for Vegetarian, 2 for Vegan, 3 for Keto, 4 for Regular): ")
    try:
        choice = int(choice)
        if 1 <= choice <= 4:
            print(f"\nYou selected the {preference_list[choice - 1]['diet']} diet.")
        else:
            raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)
    user_chosen_diet = preference_list[choice - 1]  
    
    # Recommend recipes based on the available ingredients and user preferences
    recommended_recipes = recommend_recipes(ingredient_list, user_chosen_diet)
    
    #Creates a meal plan based on the recommended recipes and user preferences
    meal_plan = create_meal_plan(recommended_recipes, user_chosen_diet)
  
    #Creates a shopping list based on the recommended recipes and available ingredients
    shopping_list = create_shopping_list(recommended_recipes, ingredient_list)
    
    #Writes the meal plan and shopping list to a single output file
    write_output(meal_plan, shopping_list, "output.txt")
    
    #visualize data
    visualize_nutrition(meal_plan)
    
