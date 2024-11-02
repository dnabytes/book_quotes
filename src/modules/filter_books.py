def hit(book, query):
    if query == book.book_id:
        return True
    if query in book.book_name.casefold().split():
        return True
    if query in book.str_authors.casefold().split():
        return True
    if query in book.tags:
        return True
    if query == book.reading_year:
        return True
    return False

def filter_books(books, query):
    if query == 'all':
        return books
    if query == 'favs':
        return [book for book in books if book.is_favorite]
    return [book for book in books if hit(book, query)]
