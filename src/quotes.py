#!/usr/bin/python3
from modules.get_books import get_books
from modules.get_authors import get_authors
from modules.filter_books import filter_books
from modules.print_entries import print_books_table, print_book_quotes_markdown, print_authors_table, print_tags_table, print_quotes_markdown
from modules.utils import go_to_quotes_dir, get_args, get_tags, filter_quotes

#TODO hash checking

def main():
    go_to_quotes_dir()
    args = get_args()
    books = get_books()

    #! SEARCH BOOKS
    if args.show_books:
        query = args.show_books.casefold()
        filtered_books = filter_books(books, query)
        if len(filtered_books) == 1: # if only one book was found, print quotes
            print_book_quotes_markdown(filtered_books[0])
        elif len(filtered_books) > 1:
            print_books_table(filtered_books)
        else:
            print('No books found.')

    #! SEARCH QUOTES
    elif args.show_quotes:
        query = args.show_quotes.casefold()
        quotes = filter_quotes(books, query)
        if quotes:
            print_quotes_markdown(quotes)
        else:
            print('No quotes found.')

    #! PRINT AUTHORS TABLE
    elif args.show_authors:
        authors = get_authors(books)
        print_authors_table(authors)

    #! PRINT TAGS TABLE
    elif args.show_tags:
        tags = get_tags(books)
        print_tags_table(tags)

if __name__ == '__main__':
    main()
