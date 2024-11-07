
def visualize_nutrition(meal_plan):
    
    for day in meal_plan.keys():
        # Format the data for plotting
        print(day, meal_plan[day])
