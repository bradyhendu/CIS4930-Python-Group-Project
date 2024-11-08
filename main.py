from input import read_ingredients, read_preferences
from recipes import recommend_recipes
from output import write_output
from visualize import visualize_nutrition
import sys

#outside imports
#import matplotlib.pyplot as plt

def create_meal_plan(recommended_recipes, user_diet):
    # Creates a meal plan based on the recommended recipes and user preferences
    meal_plan = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
   
    print(user_diet)
    for recipe in recommended_recipes:
        print(recipe)
        
    for day in meal_plan.keys():
        meal_plan[day] = ["Add recipes here with algorithm"]
    
    return meal_plan

def create_meal_plan(recommended_recipes, user_chosen_diet):
    """Creates a meal plan based on the recommended recipes and user preferences."""
    
    # meal plan dictionary with each day of the week
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

def write_output(meal_plan, shopping_list, output_file):
    """Writes the meal plan and shopping list to a single output file."""
    with open(output_file, 'w') as file:
        # Writing the meal plan to the file
        file.write("Weekly Meal Plan:\n")
        for day, recipes in meal_plan.items():
            file.write(f"{day}:\n")
            if recipes:
                for recipe in recipes:
                    recipe_name = list(recipe.keys())[0]
                    file.write(f"  - {recipe_name}\n")
                    ingredients = recipe[recipe_name].get("ingredients", {})
                    file.write("    Ingredients:\n")
                    for ingredient, quantity in ingredients.items():
                        file.write(f"      - {ingredient}: {quantity}\n")
            else:
                file.write("  - No recipe assigned\n")
            file.write("\n")
        
        # Writing the shopping list to the file
        file.write("\nShopping List:\n")
        if shopping_list:
            for item in shopping_list:
                file.write(f"  - {item['ingredient']}: {item['quantity']}\n")
        else:
            file.write("  - No items needed\n")




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
    
    # TODO: enter and fix above function, and then uncomment below function call 
    # recommended_recipes, user_chosen_diet = recommend_recipes(ingredient_list, user_chosen_diet)
    
    
    #Creates a meal plan based on the recommended recipes and user preferences
    meal_plan = create_meal_plan(recommended_recipes, user_chosen_diet)
  
    #Creates a shopping list based on the recommended recipes and available ingredients
    shopping_list = create_shopping_list(recommended_recipes, ingredient_list)
    
    #Writes the meal plan and shopping list to a single output file
    write_output(meal_plan, shopping_list, "output.txt")
    
    #visualize data
    visualize_nutrition(meal_plan)
    
