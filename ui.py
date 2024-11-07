"""File for user interface functions. """
import api_maps, api_weather, api_nps


def display_menu_get_choice(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ')
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')

            
# Function responsible for getting data from user will be given to callApis
 # Need to add data validation!!
def getData():
    np = input('Enter national park name (e.g. "Grand Canyon National Park"): ')
    #month = input('Enter number of month you want to visit: ')
    try:
        user_input = input("Please enter a month number (1-12): ")  # Get input as a string
        month = int(user_input)  # Convert input to an integer
        # Optionally, check if the month is within the valid range
        if month < 1 or month > 12:
            print(f"Please enter a valid month number between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    # location = input('Enter your location: ')
    return np, month
            
    
# Function responsible for printing API results in a nice format
def printPrettyResults(park_name, park_description, weather, distance): # todo add other arguments: # todo add other arguments

    print(f'National Park: {park_name}')
    print(f'Park Description: {park_description}')
    print(f'Weather Info: {weather}')
    print(f'Travel Info: {distance}')
    #TODO display somehow
