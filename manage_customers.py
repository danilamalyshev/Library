import csv
import os
import logging
from utils import generate_id
from utils import check_username
from manage_books import delete_book


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='DATABASE/app.log',
    filemode='w'
)

file_path_book = "Bookstore/book.csv"

def add_user():
    field_names = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone', 'Password', 'Administrator']

    with open('Bookstore/customer.csv', mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    new_user = {
        'Id': str(generate_id()),
        'Username': check_username(),
        'Name': input('Print name: '),
        'Surname': input('Print surname: '),
        'Email': input('Print email: '),
        'Phone': str(input('Print phone: ')),
        'Password': input('Print password: '),
        'Administrator': 'No'
    }
    reader.append(new_user)

    with open('Bookstore/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(reader)

    file_path = os.path.join('DATABASE', f"{new_user['Id']}.txt")

    with open(file_path, mode='w', encoding='utf-8') as file:
        print('File created')


def delete_user(delete_id, delete_username):
    headers = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone', 'Password', 'Administrator']

    with open('Bookstore/customer.csv', mode='r', encoding='utf-8') as file:
        users = list(csv.DictReader(file))

    result = []
    for user in users:
        match_id = delete_id and user['Id'] == str(delete_id)
        match_username = delete_username and user['Username'] == delete_username
        if not (match_id or match_username):
            result.append(user)

    with open('Bookstore/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(result)


def change_user_data(user_data):
    fieldnames = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone', 'Password', 'Administrator']

    updated_users = []
    search_value = user_data.strip()
    with open('Bookstore/customer.csv', mode='r', encoding='utf-8') as file:
        users = list(csv.DictReader(file))

    user_found = False

    for user in users:
        if user['Id'] == search_value or user['Username'] == search_value:
            print(f'User found: {user}')
            print('Select fields to update (enter numbers separated by commas or enter 0 to update all):')
            options = [
                '0 - Update all',
                '1 - Id',
                '2 - Username',
                '3 - Name',
                '4 - Surname',
                '5 - Email',
                '6 - Phone',
                '7 - Password',
                '8 - Administrator'
            ]
            for option in options:
                print(option)

            selected = input("Your selection: ").split(',')
            selected = [s.strip() for s in selected]

            if '0' in selected:
                user['Id'] = generate_id()
                user['Username'] = check_username()
                user['Name'] = input('Enter new name: ')
                user['Surname'] = input('Enter new surname: ')
                user['Email'] = input('Enter new email: ')
                user['Phone'] = input('Enter new phone: ')
                user['Password'] = input('Enter new password: ')
                user['Administrator'] = input('Administrator (Yes/No): ')
            else:
                if '1' in selected:
                    user['Id'] = generate_id()
                if '2' in selected:
                    user['Username'] = check_username()
                if '3' in selected:
                    user['Name'] = input('Enter new name: ')
                if '4' in selected:
                    user['Surname'] = input('Enter new surname: ')
                if '5' in selected:
                    user['Email'] = input('Enter new email: ')
                if '6' in selected:
                    user['Phone'] = input('Enter new phone: ')
                if '7' in selected:
                    user['Password'] = input('Enter new password: ')
                if '8' in selected:
                    user['Administrator'] = input('Administrator (Yes/No): ')

            user_found = True

        updated_users.append(user)

    if not user_found:
        print('User not found')
        return

    with open('Bookstore/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_users)


def buy_book():

    book_format = ['ID', 'Title', 'Author', 'Year', 'Count', 'Modified']
    headers = book_format


    with open(file_path_book, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    buying_process = True

    while buying_process:
        book_found = False
        purchase_successful = False
        book_name = input("Enter name of the book you want to buy: ")

        for book in reader:
            if book['Title'] == book_name:
                book_found = True

                while True:
                    try:
                        count_of_books_to_buy = int(input("Enter number of books to buy: "))
                        if count_of_books_to_buy <= 0:
                            print("Please enter a positive number.\n")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                        logging.warning("ValueError: User entered invalid number input.")

                count_of_books_in_stock = int(book['Count'])

                if count_of_books_to_buy > count_of_books_in_stock:
                    print("There are only " + book['Count'] + " books in stock.\n")

                    while True:
                        try:
                            count_of_books_to_buy = int(input("Enter number of books to buy: "))
                            if count_of_books_to_buy <= 0:
                                print("Please enter a positive number.")
                                continue
                            if count_of_books_to_buy > count_of_books_in_stock:
                                print("There are only " + book['Count'] + " books in stock.")
                                continue
                            break
                        except ValueError:
                            print("Please enter a valid number.")
                            logging.warning("ValueError: User entered invalid number input.")

                if count_of_books_to_buy == count_of_books_in_stock:
                    delete_book(delete_bname=book['Title'])
                    print("Thank you for buying book " + book['Title'] + " in amount of " +
                          str(count_of_books_to_buy) + " books.")
                    reader.remove(book)
                    purchase_successful = True
                    break

                else:
                    book['Count'] = str(count_of_books_in_stock - count_of_books_to_buy)
                    print("Thank you for buying book " + book['Title'] + " in amount of " +
                          str(count_of_books_to_buy) + " books.")
                    purchase_successful = True
                    break

        if not book_found:
            print("Book not found. Try again.\n")
            continue

        if purchase_successful:
            with open(file_path_book, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(reader)
            buying_process = False


buy_book()
# add_user()
# del_id = '1241'
# del_uname = 'dfh'
# delete_user(delete_id=del_id)
# delete_user(delete_username=del_uname)
# change_user_data(user_data='6894')
