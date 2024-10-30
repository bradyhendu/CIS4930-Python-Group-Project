import input
from recipes import recommend_recipes

if __name__ == '__main__':
    ingredient_list = input.read_ingredients("ingredients.csv")
    preference_list = input.read_preferences("preferences.json")
    recommened_recipies = recommend_recipes(ingredient_list, preference_list)

    #print the recommended recipes
    print("Recommended recipes:")
    for recipe in recommened_recipies:
        print(recipe)
    
    
    