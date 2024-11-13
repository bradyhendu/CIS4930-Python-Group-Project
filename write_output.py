def write_output(meal_plan, daily_nutrition, shopping_list, output_file):
    """Writes the meal plan and shopping list to a single output file."""
    with open(output_file, 'w') as file:
        # Writing the meal plan to the file
        file.write("Weekly Meal Plan:\n")
        for day, nutrition in daily_nutrition:
            
            file.write(f"{day}:\n")
            file.write(f"\tNutrition: {nutrition}\n")
            if day in meal_plan:
                
                for recipe_name in meal_plan[day]:
                    file.write(f"\t- {recipe_name}\n")
            else:
                file.write("\t- No recipe assigned\n")
            file.write("\n")
        
        # Writing the shopping list to the file
        file.write("\nShopping List:\n")
        if shopping_list:
            for item in shopping_list:
                file.write(f"  - {item['ingredient']}: {item['quantity']}\n")
        else:
            file.write("  - No items needed\n")

