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
        self.cvs_file = 'ingredients.csv'
        self.json_file = 'preferences.json'
    
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
        recommended_recipes = [{"Pancakes": {"ingredients": {"Flour": 100, "Milk": 200}}}]
        
        user_preferences = {"Dietary Restrictions": "None"}
        
        expected_meal_plan = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }
        
        result = create_meal_plan(recommended_recipes, user_preferences)
        self.assertSetEqual(result, expected_meal_plan, "The meal plan does not math the expected structure.")
        
    def test_create_shopping_list(self):
        recommended_recipes = [{"Pancakes": {"ingredients": {"Flour": 100, "Milk": 200}}}]
        
        available_ingredients = [
            {"name": "Flour", "quantity": 50},
            {"name": "Sugar", "quantity": 200}
            ]
        
        expected_shopping_list = [
            {"ingredient": "Flour", "quantiy": 50},
            {"ingredient": "Milk", "quantity": 200}
        ]
        
        result = create_shopping_list(recommended_recipes, available_ingredients)
        self.assertEqual(result, expected_shopping_list, "The shopping list does not match the expected output.")
        
        
if __name__ == '__main__':
            # Open the output file in write mode
    with open('test_results.txt', 'w') as f:
        # Create a test suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestMealPlanner)
        # Run the tests and write the results to the file, verbosity means the level of detail in the output
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
        
        
            