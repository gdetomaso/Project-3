from unittest import TestCase
from unittest.mock import patch
from api_nps import get_national_park_info_from_api


class TestNationalParksInfo(TestCase):
    @patch('api_nps.get_national_park_info_from_api')
    def test_park_name(self, mock_park_info):  # mock_park_info takes place of get_national_park_info_from_api
        example_park_info_response = {"fullName": "Yellowstone National Park"}  # mock JSON response
        mock_park_info.return_value = [example_park_info_response] # return value is equal to mock response
        result, _ = get_national_park_info_from_api("yell") # call function with correct four-letter code
        expected = "Yellowstone National Park"
        self.assertEqual(expected, result.name)


    @patch('api_nps.get_national_park_info_from_api')
    def test_unknown_park(self, mock_park_info):
        unknown_park_example_response = {"fullName": None}
        mock_park_info.return_value = [unknown_park_example_response]
        result, _ = get_national_park_info_from_api(None)
        expected = None
        self.assertEqual(expected, result)







