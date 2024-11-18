from input import read_ingredients, read_preferences
from recipes import recommend_recipes
from write_output import write_output
from visualize import visualize_nutrition
from create_meal_plan import create_meal_plan
import sys

#outside imports
#import matplotlib.pyplot as plt


def create_shopping_list(recommended_recipes, available_ingredients):
    # Loop through the recommended recipes and create a shopping list based on the missing ingredients
    available_ingredient_names = {ingredient["name"] for ingredient in available_ingredients}
    shopping_list = {}
    
    for recipe in recommended_recipes:
        for recipe_name, recipe_details in recipe.items():
            if recipe_name == "nutrition":
                continue
            
            for ingredient, quantity in recipe_details["ingredients"].items():
                if ingredient not in available_ingredient_names:
                    if ingredient in shopping_list:
                        shopping_list[ingredient] += quantity
                    else:
                        shopping_list[ingredient] = quantity
                else:
                    # If the ingredient is available, check if the quantity is sufficient
                    available_quantity = int(next((item["quantity"] for item in available_ingredients if item["name"] == ingredient), 0))
                    if available_quantity < quantity:
                        if ingredient in shopping_list:
                            shopping_list[ingredient] += (quantity - available_quantity)
                        else:
                            shopping_list[ingredient] = (quantity - available_quantity)
    
    # Convert the shopping list dictionary to a list of dictionaries
    shopping_list = [{"ingredient": ingredient, "quantity": quantity} for ingredient, quantity in shopping_list.items()]
    
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
    meal_plan, daily_nutrition = create_meal_plan(recommended_recipes, user_chosen_diet)
  
    #Creates a shopping list based on the recommended recipes and available ingredients
    shopping_list = create_shopping_list(recommended_recipes, ingredient_list)
    
    #Writes the meal plan and shopping list to a single output file
    write_output(meal_plan, daily_nutrition, shopping_list, "output.txt")
    
    #visualize data
    visualize_nutrition(daily_nutrition)
    
