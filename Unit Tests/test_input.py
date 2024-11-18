import unittest
import json
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from input import read_ingredients, read_preferences

class TestInput(unittest.TestCase):
    
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
        
if __name__ == '__main__':
            # Open the output file in write mode
    with open('test_results.txt', 'w') as f:
        # Create a test suite
        suite = unittest.TestLoader().loadTestsFromTestCase(TestInput)
        # Run the tests and write the results to the file
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
        
        
            