import input
from recipes import recommend_recipes

if __name__ == '__main__':
    # Read the ingredients and preferences from the input files
    ingredient_list = input.read_ingredients("ingredients.csv")
    preference_list = input.read_preferences("preferences.json")
    
    # Recommend recipes based on the available ingredients and user preferences
    recommened_recipies = recommend_recipes(ingredient_list, preference_list)
    
    #Creates a meal plan based on the recommended recipes and user preferences
    
    
    #Creates a shopping list based on the recommended recipes and available ingredients
    
    #Writes the meal plan and shopping list to a single output file
    
    