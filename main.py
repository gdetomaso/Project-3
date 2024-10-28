"""Program that uses apis to inform user of weather, distance and park info
of the national park they want to visit"""
from api_nps import get_park_postal_code, show_park_info
from menu import Menu
import ui

#main function that runs the entire program
def main(postal_code):
    menu = create_menu()
    parks_zip = show_park_info(national_park_info=postal_code)
    print(parks_zip)


    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


# uses add_option from menu.py to add options to the menu


def create_menu():
    menu = Menu()
    menu.add_option('1', 'Search Parks', search)
    menu.add_option('2', 'Bookmark', bookmark)
    menu.add_option('3', 'View Bookmarks', view_bookmarks)
    menu.add_option('Q', 'Quit', quit)
    return menu


# Need to ask user for National park, month of visit, and current location.
def search():
    #getData() gets required data from user National park, month of visit, and current location
    park_entered, month_entered, distance = ui.get_data()
    #call each api with data
    ui.call_apis(park_entered, month_entered, distance)
    #takes the returned data from the APIs and prints it to the user in a nice format
    print_pretty_results(park_entered, month_entered, distance)

def bookmark():
    print('Bookmarking')


def view_bookmarks():
    print('Viewing Bookmarks')


def quit():
    print('Quitting')


# Function responsible for printing API results in a nice format
 def print_pretty_results(np, month, location):
    print('National Park: ' + np)
    print('Month: ' + month)
    print('Distance: ' + location)

main(postal_code=any)