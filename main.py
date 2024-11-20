from input import read_ingredients, read_preferences
from recipes import recommend_recipes
from write_output import write_output
from visualize import visualize_nutrition
from create_meal_plan import create_meal_plan
from shopping import create_shopping_list
import sys

#outside imports
#import matplotlib.pyplot as plt

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
    
    print("\nMeal plan and shopping list have been written to output.txt, please review that now.\n")
    input = input("Would you like to visualize the nutrition data? (yes/no): ")
    if input.lower() == "yes":
        visualize = True
    else:
        visualize = False
    
    #visualize data
    if visualize:
        visualize_nutrition(daily_nutrition)
    
