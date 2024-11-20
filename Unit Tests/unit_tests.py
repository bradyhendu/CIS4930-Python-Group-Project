import unittest
import json
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from input import read_ingredients, read_preferences
from create_meal_plan import create_meal_plan
from shopping import create_shopping_list
from write_output import write_output


class TestMealPlanner(unittest.TestCase):
    
    def setUp(self):
        self.cvs_file = 'test_ingredients.csv'
        self.json_file = 'test_preferences.json'
    
        with open(self.cvs_file, 'w') as f:
            f.write("name,quantity,unit\n")
            f.write("sugar,100,grams\n")
            f.write("flour,1000,grams\n")
            
        sample_data = {
           "user_preferences": ["vegetarian", "low_carb"]              
        }
        with open(self.json_file, 'w') as f:
            json.dump(sample_data, f)
            
    def tearDown(self):
        os.remove(self.cvs_file)
        os.remove(self.json_file)
        
    def test_read_ingredients(self):
        expected_output = [
            {"name": "sugar", "quantity": "100", "unit": "grams"},
            {"name": "flour", "quantity": "1000", "unit": "grams"}
        ]
        result = read_ingredients(self.cvs_file)
        self.assertEqual(result, expected_output)
        
    def test_read_preferences(self):
        expected_output = ["vegetarian", "low_carb"]
        result = read_preferences(self.json_file)
        self.assertEqual(result, expected_output)
    
    def test_create_meal_plan(self):
        recommended_recipes = [{'Pancakes': {'ingredients': {'flour': 100, 'egg': 1}, 'diet': 'vegetarian'}, 'nutrition': {'calories': 700, 'protein': 40, 'carbs': 120, 'fat': 35, 'fiber': 25}}]
        
        user_preferences = {'diet': 'regular', 'nutritional_goals': {'calories': 2200, 'protein': 70, 'carbs': 150, 'fat': 100}}
        
        expected_meal_plan = {
            'Monday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Tuesday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Wednesday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Thursday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Friday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Saturday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Sunday': ['Pancakes', 'Pancakes', 'Pancakes']
        }

        expected_daily_nutrition = [
            ['Monday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Tuesday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Wednesday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Thursday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Friday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Saturday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Sunday', {'calories': 2100, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}]
        ]
        
        result = create_meal_plan(recommended_recipes, user_preferences)
        self.assertEqual(result, (expected_meal_plan, expected_daily_nutrition), "The meal plan does not match the expected structure.")
        
    def test_create_shopping_list(self):
        recommended_recipes = [{'Pancakes': {'ingredients': {'flour': 100, 'egg': 1}, 'diet': 'vegetarian'}, 'nutrition': {'calories': 850, 'protein': 40, 'carbs': 120, 'fat': 35, 'fiber': 25}}]
        
        available_ingredients = [
            {"name": "flour", "quantity": 50},
            {"name": "fugar", "quantity": 200}
        ]
        
        expected_shopping_list = [
            {"ingredient": "flour", "quantity": 50},
            {"ingredient": "egg", "quantity": 1}
        ]
    
        
        result = create_shopping_list(recommended_recipes, available_ingredients)
        self.assertEqual(result, expected_shopping_list, "The shopping list does not match the expected output.")
    
    def test_write_output(self):
        meal_plan = {
            'Monday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Tuesday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Wednesday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Thursday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Friday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Saturday': ['Pancakes', 'Pancakes', 'Pancakes'],
            'Sunday': ['Pancakes', 'Pancakes', 'Pancakes']
        }

        daily_nutrition = [
            ['Monday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Tuesday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Wednesday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Thursday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Friday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Saturday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}],
            ['Sunday', {'calories': 2550, 'protein': 120, 'carbs': 360, 'fat': 105, 'fiber': 75}]
        ]

        shopping_list = [
            {"ingredient": "flour", "quantity": 50},
            {"ingredient": "egg", "quantity": 1}
        ]

        output_file = 'test_output.txt'
        
        # Call the function to write the output
        write_output(meal_plan, daily_nutrition, shopping_list, output_file)
        
        # Read the contents of the output file
        with open(output_file, 'r') as file:
            output_content = file.read()
        
        #If this fails, we know the function did not write anything to the file, as in it failed
        self.assertIsNotNone(output_content, "The output file is empty.")
        
        # Clean up the output file
        os.remove(output_file)
        
        
if __name__ == '__main__':
    # Ensure the Unit Tests directory exists
    os.makedirs('Unit Tests', exist_ok=True)
    
    #delete the output file if it exists
    try:
        os.remove('Unit Tests/test_results.txt')
    except:
        pass
    
    # Open the output file in write mode
    with open('Unit Tests/test_results.txt', 'w') as f:
        # Create a test suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestMealPlanner)
        # Run the tests and write the results to the file, verbosity means the level of detail in the output
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
        
            