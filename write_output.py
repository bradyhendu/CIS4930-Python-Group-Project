def write_output(meal_plan, shopping_list, output_file):
    """Writes the meal plan and shopping list to a single output file."""
    with open(output_file, 'w') as file:
        # Writing the meal plan to the file
        file.write("Weekly Meal Plan:\n")
        for day, recipes in meal_plan.items():
            file.write(f"{day}:\n")
            if recipes:
                for recipe_name in recipes:
                    file.write(f"  - {recipe_name}\n")
                    ingredients = recipes[recipe_name].get("ingredients", {})
                    file.write("    Ingredients:\n")
                    for ingredient, quantity in ingredients.items():
                        file.write(f"      - {ingredient}: {quantity}\n")
            else:
                file.write("  - No recipe assigned\n")
            file.write("\n")
        
        # Writing the shopping list to the file
        file.write("\nShopping List:\n")
        if shopping_list:
            for item in shopping_list:
                file.write(f"  - {item['ingredient']}: {item['quantity']}\n")
        else:
            file.write("  - No items needed\n")

