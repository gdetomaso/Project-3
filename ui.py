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
# todo add data validation!!
def get_data():
    park_entered = input('Enter park name: ')
    month_entered = input('Enter month: ')
    return park_entered, month_entered


# Function responsible for calling all 3 APIs with data from user
def call_apis(park_entered, month_entered, distance):

    parks1 = api_nps.getNps(park_entered)
    month1 = api_weather.getWeather(month_entered)
    distance1 = api_maps.getMaps(distance)
    #retuns data from 3 apis
    return parks1, month1, distance1
