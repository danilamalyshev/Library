import csv
import os
import logging
from utils import *

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def add_user():
    field_names = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone','Password','Administrator']

    with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
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

    with open('../DATABASE/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(reader)

    file_path = os.path.join('../DATABASE', f"{new_user['Id']}.txt")

    with open(file_path, mode='w', encoding='utf-8') as file:
        print('File created')

def delete_user(delete_id, delete_username):
    headers = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone','Password','Administrator']

    with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
        users = list(csv.DictReader(file))

    result = []
    for user in users:
        match_id = delete_id and user['Id'] == str(delete_id)
        match_username = delete_username and user['Username'] == delete_username
        if not (match_id or match_username):
            result.append(user)

    with open('../DATABASE/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(result)

def change_user_data(user_data):
    fieldnames = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone', 'Password', 'Administrator']

    updated_users = []
    search_value = user_data.strip()
    with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
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

    with open('../DATABASE/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_users)


# add_user()
# del_id = '1241'
# del_uname = 'dfh'
# delete_user(delete_id=del_id)
# delete_user(delete_username=del_uname)
change_user_data(user_data='6894')