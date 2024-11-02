import os
import sys
import argparse
from classes.Quote import Quote

def go_to_quotes_dir():
    quotes_path = os.environ.get('bookquotes')
    if quotes_path is None:
        print('bookquotes env var not configured.')
        sys.exit(1)
    os.chdir(quotes_path)

def get_args():
    parser = argparse.ArgumentParser(prog='quotes', description='Manage your book quotes')
    parser.add_argument('-b', '-books', metavar='', dest='show_books', help='search books by book id, book name, author, tag or reading year ("all" to show all books / "favs" to show favorites)')
    parser.add_argument('-q', '-quotes', metavar='', dest='show_quotes', help='search quotes by a query word')
    parser.add_argument('-a', '-authors', action='store_true', dest='show_authors', help='show authors table')
    parser.add_argument('-t', '-tags', action='store_true', dest='show_tags', help='show tags table')
    args = parser.parse_args()
    if not any([args.show_books, args.show_quotes, args.show_authors, args.show_tags]):
        parser.print_help()
        sys.exit()
    return args

def get_tags(books):
    tag_list = [tag for book in books for tag in book.tags]
    tags = {tag: tag_list.count(tag) for tag in set(tag_list)}
    return tags

def filter_quotes(books, query):
    quotes = [Quote(book.book_name, book.authors, quote) for book in books for quote in book.quotes if query in quote]
    return quotes
