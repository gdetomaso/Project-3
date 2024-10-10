from modelBookmark import BookMark
from peewee import fn
        
def delete_bookmark(bookmark):
    """ Removes book from store. Raises BookError if book not in store. 
    :param book the Book to delete """

    rows_deleted = BookMark.delete().where(BookMark.id == bookmark.id).execute()
    if not rows_deleted:
        raise BookError('Tried to delete bookmark that doesn\'t exist')


def delete_all_bookmarks():
    """ Deletes all bookmarks from database """
    BookMark.delete().execute()


def get_bookmark_by_id(bookmark_id):
    """ Searches list for a Bookmark with given ID,
    :param id the ID to search for
    :returns the book, if found, or None if book not found.
    """
    return BookMark.get_or_none(BookMark.id == bookmark_id)


def book_search(term):
    """ Searches the database for bookmarks that contain a park name. Case insensitive.
    Makes partial matches
    :param term the search term
    :returns a list of books with author or title that match the search term. The list will be empty if there are no matches.
    """

    query = BookMark.select().where( ( fn.LOWER(BookMark.parkdata).contains(term.lower() ) ) )
    return list(query)



def get_all_bookmarks():
    """ :returns entire bookmark list """

    query = BookMark.select()
    return list(query)


def book_count():
    """ :returns the number of bookmarks in the database """
    
    return BookMark.select().count()



class BookError(Exception):
    """ For BookStore errors. """
    pass