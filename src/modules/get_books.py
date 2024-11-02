import os
import sys
from classes.Book import Book

def get_book_name_authors(line, file_name):
    is_favorite = line.strip().endswith('*')
    try:
        book_name, authors = line.strip('*#\n').split('/')
        authors = [author.strip() for author in authors.split('&')]
    except ValueError:
        print(f'Wrong format in book header -> {line.strip()} in {file_name}')
        print('The format should be book_name/author1 & author2 & authorn')
        sys.exit(1)
    return book_name, authors, is_favorite

def get_md_file_content(md_file_name):
    year = md_file_name.split('.')[0] # md name: year.md
    if len(year) != 4 or not year.isdigit():
        sys.exit(f'{md_file_name} file name is in the wrong format')
    with open(md_file_name, 'r', encoding="utf-8") as file_handle:
        lines = [line for line in file_handle if line.strip()]
    assert lines, (f'{md_file_name} is empty')
    return lines, year

def read_md_file(md_file_name):
    books = []
    lines, year = get_md_file_content(md_file_name)
    for line in lines:
        if line.startswith('#'):
            book_id = f'{year[-2:]}-{len(books)+1}'
            book_name, authors, is_favorite = get_book_name_authors(line, md_file_name)
            books.append(Book(book_id, book_name, authors, year, is_favorite))
        elif line.startswith('[') and line.strip().endswith(']') and line.strip() != '[]': # tags
            books[-1].tags = [tag.strip() for tag in line.lower().strip('[]\n').split(',')]
        elif line.startswith('*'): # new quote starts
            books[-1].quotes.append(line.lstrip('* '))
        else: # more lines to last quote
            books[-1].quotes[-1] +=  '\n  ' + line # newline in markdown
    return books

def get_books():
    quotes_files = sorted([xfile for xfile in os.listdir(os.curdir) if xfile.endswith('.md')])
    books = [book for md_file_name in quotes_files for book in read_md_file(md_file_name)]
    if not books:
        sys.exit('No quotes found')
    return books
