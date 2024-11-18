import matplotlib.pyplot as plt
import numpy as np

def visualize_nutrition(daily_nutrition):
    
    days = [day[0] for day in daily_nutrition]
    calories = [day[1]['calories'] for day in daily_nutrition]
    protein = [day[1]['protein'] for day in daily_nutrition]
    carbs = [day[1]['carbs'] for day in daily_nutrition]
    fat = [day[1]['fat'] for day in daily_nutrition]
    fiber = [day[1]['fiber'] for day in daily_nutrition]

    bar_width = 0.15
    index = np.arange(len(days))

    plt.bar(index, calories, bar_width, label='Calories', color='r')
    plt.bar(index + bar_width, protein, bar_width, label='Protein', color='g')
    plt.bar(index + 2 * bar_width, carbs, bar_width, label='Carbs', color='b')
    plt.bar(index + 3 * bar_width, fat, bar_width, label='Fat', color='y')
    plt.bar(index + 4 * bar_width, fiber, bar_width, label='Fiber', color='m')

    plt.xlabel('Day')
    plt.ylabel('Nutritional Values')
    plt.title('Daily Nutrition')
    plt.xticks(index + 2 * bar_width, days)
    plt.legend()

    plt.tight_layout()
    plt.show()
