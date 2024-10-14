import input

if __name__ == '__main__':
    ingredient_list = input.read_ingredients("ingredients.csv")
    preference_list = input.read_preferences("preferences.json")
    
    #for testing
    for ingredient in ingredient_list:
        print(ingredient)
    
    for preference in preference_list:
        print(preference)
    