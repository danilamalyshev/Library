import csv
from utils import generate_id

book_format = ['ID', 'Title', 'Author', 'Year', 'Count', 'Modified']


def add_book(new_book):
    with open("../ DATABASE/ book.csv", "r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))

    reader.append(new_book)

    with open("../ DATABASE/ book.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=book_format)
        writer.writeheader()
        writer.writerows(reader)


new_id = str(generate_id())
new_book_title = input("Enter new book title: ")
new_book_author = input("Enter new book author: ")
new_book_year = input("Enter new book year: ")
new_book_count = input("Enter new book count: ")
new_book_modified = input("Enter new book modified: ")

new_book = {
    'ID': new_id,
    'Title': new_book_title,
    'Author': new_book_author,
    'Year': new_book_year,
    'Count': new_book_count,
    'Modified': new_book_modified
}

add_book(new_book)
