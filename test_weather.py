import unittest 
from unittest import TestCase
import api_weather
import os 
import json 

class TestWeather(TestCase):

    def test_get_weather_description_for_month(self):

        # List from example response JSON, read from a file to avoid very large JSON object here 
        with open(os.path.join('test_data', 'example_weather_response_june_minneapolis.json')) as f:
            response = json.load(f)
            weather_data = response['days']
        
        actual_description = api_weather.get_description_for_month(weather_data, 6)
        expected_description = 'In June the average high and low temperatures are 83.93F and 64.01F and the average precipitation is 0.04 inches.'
        self.assertEqual(expected_description, actual_description)
        

if __name__ == '__main__':
    unittest.main()