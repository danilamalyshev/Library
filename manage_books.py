import csv
from utils import *

file_path = "Bookstore/book.csv"


def add_book():
    book_format = ['ID', 'Title', 'Author', 'Year', 'Count', 'Modified']
    book_exists = False

    new_book_title = input("Enter new book title: ")

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    for book in reader:
        if book['Title'] == new_book_title:
            new_book_modified = input("Enter modified value: ")
            book['Count'] = str(int(book['Count']) + 1)
            book['Modified'] = new_book_modified
            book_exists = True
            break

    if not book_exists:
        new_book_author = input("Enter new book author: ")
        new_book_year = input("Enter new book year: ")
        new_book_count = input("Enter new book count: ")
        new_book_modified = input("Enter new book modified: ")

        new_book = {
            'ID': generate_id(),
            'Title': new_book_title,
            'Author': new_book_author,
            'Year': new_book_year,
            'Count': new_book_count,
            'Modified': new_book_modified
        }
        reader.append(new_book)

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=book_format)
        writer.writeheader()
        writer.writerows(reader)


def delete_book(delete_bid=None, delete_bname=None):
    book_format = ['ID', 'Title', 'Author', 'Year', 'Count', 'Modified']
    headers = book_format

    with open(file_path, mode='r', encoding='utf-8') as file:
        books = list(csv.DictReader(file))

    result = []
    for book in books:
        match_id = delete_bid and book['ID'] == str(delete_bid)
        match_username = delete_bname and book['Title'] == delete_bname
        if not (match_id or match_username):
            result.append(book)

    with open(file_path, mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(result)


