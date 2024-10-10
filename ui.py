"""File for user interface functions. """
import api_maps, api_weather, api_nps
from modelBookmark import BookMark
import bookmarks

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

# Function responsible for printing API results in a nice format
def printPrettyResults(np, month, location):

    print('National Park: ' + np)
    print('Month: ' + month)
    print('Location: ' + location)

# Function responsible for getting data from user will be given to callApis
# Need to add data validation!!
def getData():
    np = input('Enter data np: ')
    month = input('Enter data month: ')
    location = input('Enter data location: ')
    return np, month, location

# Function responsible for calling all 3 APIs with data from user
def callApis(np, month, location):

    np1 = api_nps.getNps(np)
    month1 = api_weather.getWeather(month)
    location1 = api_maps.getMaps(location)
    #retuns data from 3 apis
    return np1, month1, location1

#store search in a bookmark database if user says yes
def storeBookmark(np, month, location):
    if input('Would you like to save this search? (y/n)') == 'y':
        print('Saving to database...')
        return BookMark(parkdata=np, weatherdata=month, directiondata=location)
    else:
        return None

def displayBookmarks(bookmarks):
    if bookmarks:
        for bookmark in bookmarks:
            print(bookmark)
    else:
        print('No bookmarks found.')

    