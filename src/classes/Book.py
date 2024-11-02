class Book:
    def __init__(self, book_id, book_name, authors, reading_year, is_favorite):
        self.book_id = book_id
        self.book_name = book_name
        self.authors = authors
        self.str_authors = (' & ').join(self.authors)
        self.reading_year = reading_year
        self.is_favorite = is_favorite
        self.quotes = []
        self.tags = []

    def __repr__(self):
        return f'{self.book_id} {self.book_name} {self.str_authors}'
