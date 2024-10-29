"""Program that uses apis to inform user of weather, distance and park info
of the national park they want to visit"""
from api_nps import get_park_postal_code, show_park_info
import park_code_lookup
from menu import Menu
import ui
import api_manager

#main function that runs the entire program
def main():
    menu = create_menu()
    # parks_zip = show_park_info(national_park_info=postal_code)
    # print(parks_zip)


    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        if choice == 'Q':
            break


# uses add_option from menu.py to add options to the menu
def create_menu():
    menu = Menu()
    menu.add_option('1', 'Search', search)
    # menu.add_option('2', 'Bookmark', bookmark)   # only a option once user has seen day
    menu.add_option('3', 'view bookmarks', viewBookmarks)
    menu.add_option('Q', 'Quit', quit)
    return menu

# Need to ask user for National park, month of vist, and current location. 
def search():
    #getData() gets required data from user National park, month of vist, and current location
    national_park_name, month = ui.getData()

    park_code = park_code_lookup.get_four_letter_code_as_string_for_url(national_park_name)
    if park_code is None:
        pass # todo handle not found
    
    else:
        # call each api with data
        national_park_info, monthly_weather, travel_from_minneapolis = api_manager.get_national_park_info_for_park_and_month(park_code, month)
        # takes the returned data from the APIs and prints it to the user in a nice format
        ui.printPrettyResults(national_park_name, park_code, month, national_park_info, monthly_weather, travel_from_minneapolis)


def bookmark():
    print('Bookmarking')


def viewBookmarks():
    print('Viewing Bookmarks')

def quit():
    print('Quitting')



main()