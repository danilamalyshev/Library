import csv
from utils import generate_id

book_format = ['ID', 'Title', 'Author', 'Year', 'Count', 'Modified']


def add_book(new_book):
    with open("../ DATABASE/ book.csv", "r", encoding="utf-8") as file:
        reader = list(csv.reader(file))

    reader.append(new_book)

    with open("../ DATABASE/ book.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(book_format)
        writer.writerows(reader)


new_id = generate_id()
new_book_title = input("Enter new book title: ")
new_book_author = input("Enter new book author: ")
new_book_year = input("Enter new book year: ")
new_book_count = input("Enter new book count: ")
new_book_modified = input("Enter new book modified: ")

new_book_data = [new_id, new_book_title, new_book_author, new_book_year, new_book_count, new_book_modified]
add_book(new_book_data)
