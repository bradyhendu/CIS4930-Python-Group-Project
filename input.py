def read_ingredients():
    ingredients = []
    with open('ingredients.csv', 'r') as f:
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