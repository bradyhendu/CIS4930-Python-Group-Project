import json
def read_ingredients(input_file):
    ingredients = []
    with open(input_file, 'r') as f:
        for line in f:
            #skip first line
            if 'name' in line:
                continue
            
            #add to a dictionary
            ingredient = {}
            parts = line.strip().split(',')
            ingredient["name"] = parts[0]
            ingredient["quantity"] = parts[1]
            ingredient["unit"] = parts[2]
            
            #add to list of ingredients
            ingredients.append(ingredient)
    return ingredients

def read_preferences(input_file):
    preferences = []
    with open(input_file, 'r') as f:
        preferences = json.load(f)
        
        ##take the list of different user preferences in the dictionary and convert it to a list
        preferences = preferences['user_preferences']
    return preferences