"""Program that uses apis to inform user of weather, distance and park info
of the national park they want to visit"""
import peewee
import bookmarks
from menu import Menu
import ui


#main function that runs the entire program
def main():
    #create menu
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
    menu.add_option('2', 'view bookmarks', viewBookmarks)
    menu.add_option('3', 'clear bookmarks', clearBookmarks)
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
    #store search in a bookmark
    bookmark(np, month, location)
    



def bookmark(np, month, location):
    print('Bookmarking')
    bookmark = ui.storeBookmark(np, month, location)
    try:
        bookmark.save()
    except peewee.IntegrityError as e:
        print('Error saving bookmark: ', e)
        print('Bookmark not saved')



def viewBookmarks():
    print('Viewing Bookmarks')
    allBookmarks = bookmarks.get_all_bookmarks()
    ui.displayBookmarks(allBookmarks)

def clearBookmarks():
    print('Clearing Bookmarks')
    bookmarks.delete_all_bookmarks()

def quit():
    print('Quitting')




main()