""" The main function of this code is to find the four-letter code for a National Park, as assigned by the NPS.
This code asks the user to enter the park name they wish to know more about. The code uses the CSV file NPS-Unit-List (a csv copy of the NPS Excel sheet) to find the
four-letter code of the park the user entered. That four-letter code is used in api_nps.py to create the URL for the API information on that park. """

import csv

csv_park_file = 'NPS-Unit-List.csv'

def get_park_four_letter_code(csv_park_file):
    park_searched = input('Enter the name of the park you would like to visit: ')
    park_code_for_searched_park = []
    with open (csv_park_file) as f:
        reader = csv.reader(f)
        for row in reader:
            row = [element.strip() for element in row] # take out extra spaces
            if row[0] == park_searched.upper():
                park_code_for_searched_park.append(row[1])
                return park_code_for_searched_park
    return None

def get_four_letter_code_as_string_for_url(csv_park_file):
    park_four_letter_code = get_park_four_letter_code(csv_park_file)
    if park_four_letter_code:
        return''.join(park_four_letter_code) # change list to string for URL
    return None

park_code = get_four_letter_code_as_string_for_url(csv_park_file)
#print(park_code)