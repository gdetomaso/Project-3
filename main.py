"""Program that uses apis to inform user of weather, distance and park info
of the national park they want to visit"""
from menu import Menu
import ui
import park_code_lookup
import api_manager


#main function that runs the entire program
def main():
    menu = create_menu()

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
    # menu.add_option('2', 'Bookmark', bookmark) only an option if user has seen
    menu.add_option('3', 'View Bookmarks', view_bookmarks)
    menu.add_option('Q', 'Quit', quit)
    return menu


# Need to ask user for National park, month of visit, and current location.
def search():
    #getData() gets required data from user National park, month of visit, and current location

    national_park_name, month = ui.getData()

    park_code = park_code_lookup.get_four_letter_code_as_string_for_url(national_park_name)
    if park_code is None:
        print("Park not found. Please try again.")
        return

    else:
        # call each api with data
        park_name, park_description, national_park_info, monthly_weather, travel_from_minneapolis = api_manager.get_national_park_info_for_park_and_month(park_code, month)
        # takes the returned data from the APIs and prints it to the user in a nice format

        ui.printPrettyResults(park_name, park_description,None, None )


def bookmark():
    print('Bookmarking')


def view_bookmarks():
    print('Viewing Bookmarks')


def quit():
    print('Quitting')



if __name__ == '__main__':
    main()
