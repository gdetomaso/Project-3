""" The main function of this code is to find the four-letter code for a National Park, as assigned by the NPS.
The code uses the CSV file NPS-Unit-List (a csv copy of the NPS Excel sheet) to find the four-letter code of the park the user entered.
That four-letter code is used in api_nps.py to create the URL for the API information on that park. """

import csv

csv_park_file = 'NPS-Unit-List.csv'

# open CSV file, read rows and look for park name searched for in UPPER, return 4-letter code
def get_park_four_letter_code(csv_park_file, park_name_to_search_for):
    with open (csv_park_file) as f:
        reader = csv.reader(f)
        for row in reader:
            row = [element for element in row]
            if row[0] == park_name_to_search_for.upper():
                park_code_for_searched_park = (row[1]) # returns "ARCH" or "ZION" for ex.
                return park_code_for_searched_park
    return None


# returns park name as string for URL
def get_four_letter_code_as_string_for_url(park_name):
    park_four_letter_code = get_park_four_letter_code(csv_park_file, park_name)
    return park_four_letter_code


