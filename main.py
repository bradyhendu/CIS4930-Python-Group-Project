import input
from recipes import recommend_recipes
from output import write_output

#outside imports
import matplotlib.pyplot as plt

def create_meal_plan(recommended_recipes, user_preferences):
    #Creates a meal plan based on the recommended recipes and user preferences
    pass

def create_shopping_list(recommended_recipes, available_ingredients):
    #Creates a shopping list based on the recommended recipes and available ingredients
    pass



if __name__ == '__main__':
    # Read the ingredients and preferences from the input files
    ingredient_list = input.read_ingredients("ingredients.csv")
    preference_list = input.read_preferences("preferences.json")
    
    # Recommend recipes based on the available ingredients and user preferences
    recommened_recipies = recommend_recipes(ingredient_list, preference_list)
    
    #Creates a meal plan based on the recommended recipes and user preferences
    meal_plan = create_meal_plan(recommened_recipies, preference_list)
    
    #Creates a shopping list based on the recommended recipes and available ingredients
    shopping_list = create_shopping_list(recommened_recipies, ingredient_list)
    
    #Writes the meal plan and shopping list to a single output file
    write_output(meal_plan, shopping_list, "output.txt")
    
    #visualize data
    
    