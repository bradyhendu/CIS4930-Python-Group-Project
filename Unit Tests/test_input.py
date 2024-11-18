import unittest
import json
import os
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
        unittest.main()
        
        
            