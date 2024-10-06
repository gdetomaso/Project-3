"""Program that uses apis to inform user of weather, distance and park info
of the national park they want to visit"""

from menu import Menu
import ui

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
    menu.add_option('1', 'Search', search)
    menu.add_option('2', 'Bookmark', bookmark)
    menu.add_option('3', 'view bookmarks', viewBookmarks)
    menu.add_option('Q', 'Quit', quit)
    return menu

# Need to ask user for National park, month of vist, and current location. 
def search():
    #getData() gets required data from user National park, month of vist, and current location
    np, month, location = ui.getData()
    #call each api with data
    ui.callApis(np, month, location)
    #takes the returned data from the APIs and prints it to the user in a nice format
    ui.printPrettyResults(np, month, location)



def bookmark():
    print('Bookmarking')


def viewBookmarks():
    print('Viewing Bookmarks')

def quit():
    print('Quitting')




main()