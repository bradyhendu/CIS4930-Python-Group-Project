import json

"""
Reads a CSV file containing ingredient information and returns a list of dictionaries,
each representing an ingredient with its name, quantity, and unit.
Args:
    input_file (str): The path to the input CSV file.
Returns:
    list: A list of dictionaries, where each dictionary contains the keys 'name', 'quantity', and 'unit'
          representing an ingredient's details.
The function performs the following steps:
    1. Initializes an empty list to store the ingredients.
    2. Opens the specified input file in read mode.
    3. Iterates over each line in the file.
    4. Skips the first line if it contains the header 'name'.
    5. Splits each subsequent line by commas to extract the ingredient's name, quantity, and unit.
    6. Creates a dictionary for each ingredient with keys 'name', 'quantity', and 'unit'.
    7. Appends the dictionary to the list of ingredients.
    8. Returns the list of ingredient dictionaries.
"""
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

"""
Reads a JSON file containing user preferences and returns a list of preferences.
Args:
    input_file (str): The path to the input JSON file.
Returns:
    list: A list of user preferences.
The function performs the following steps:
    1. Initializes an empty list to store the preferences.
    2. Opens the specified input file in read mode.
    3. Loads the JSON data from the file.
    4. Extracts the list of user preferences from the dictionary.
    5. Returns the list of user preferences.
"""
def read_preferences(input_file):
    preferences = []
    with open(input_file, 'r') as f:
        preferences = json.load(f)
        
        ##take the list of different user preferences in the dictionary and convert it to a list
        preferences = preferences['user_preferences']
    return preferences