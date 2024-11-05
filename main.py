import input
from recipes import recommend_recipes
from output import write_output

#outside imports
#import matplotlib.pyplot as plt

def create_meal_plan(recommended_recipes, user_preferences):
    #Creates a meal plan based on the recommended recipes and user preferences
    pass

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
    ingredient_list = input.read_ingredients("ingredients.csv")
    preference_list = input.read_preferences("preferences.json")
    
    # Recommend recipes based on the available ingredients and user preferences
    recommened_recipies = recommend_recipes(ingredient_list, preference_list)
    
    #Creates a meal plan based on the recommended recipes and user preferences
    meal_plan = create_meal_plan(recommened_recipies, preference_list)
    
    #Creates a shopping list based on the recommended recipes and available ingredients
    shopping_list = create_shopping_list(recommened_recipies, ingredient_list)
    print(shopping_list)
    
    #Writes the meal plan and shopping list to a single output file
    write_output(meal_plan, shopping_list, "output.txt")
    
    #visualize data
    
    