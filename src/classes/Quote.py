class Quote:
    def __init__(self, book_name, authors, quote):
        self.book_name = book_name
        self.authors = authors
        self.str_authors = (' & ').join(self.authors)
        self.quote = quote
