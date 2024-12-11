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

    while True:  # allow user to re-try 
        try:
            user_input = input("Please enter a month number (1-12): ")  # Get input as a string
            month = int(user_input)  # Convert input to an integer
            # Optionally, check if the month is within the valid range
            if month < 1 or month > 12:
                print(f"Please enter a valid month number between 1 and 12.")
            else: 
                # data is a number between 1 and 12, stop loop
                break 
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    # location = input('Enter your location: ')
    return np, month
            
    
# Function responsible for printing API results in a nice format
def printPrettyResults(results, park_code, month): # todo add other arguments: # todo add other arguments

    if results.get('park_error'):
        print(f'Sorry, could not get any data for {park_code}')
    else:
        park_data = results.get('park_info')
        # assume this a NationalPark object,
        print(park_data) # prints the result of __str__ method in NationalPark

    weather_description = results.get('weather_description')
    if weather_description:
        print(f'Weather: {weather_description}')
    else:
        print('Sorry, could not get weather')

    travel_description = results.get('travel_description')
    if travel_description:
        print(f'Travel: {travel_description}')
    else:
        print('Sorry, could not get travel information')

    
    