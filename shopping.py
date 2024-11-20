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
