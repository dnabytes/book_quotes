from classes.Author import Author

def get_authors(books):
    authors = {author: Author(author) for author in set(author for book in books for author in book.authors) }
    for book in books:
        for author in book.authors:
            authors[author].books.append(book)
            authors[author].tags = list(set(authors[author].tags + book.tags))

    authors = list(authors.values())
    authors.sort(key = lambda x: x.name)

    return authors
