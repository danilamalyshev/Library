import csv
from Bookstore.utils import *

file_path = '../DATABASE/customer.csv'


def add_user(new_user):
    field_names = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone']

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    reader.append(new_user)

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(reader)


def delete_user(delete_id=None, delete_username=None):
    headers = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone']

    with open(file_path, mode='r', encoding='utf-8') as file:
        users = list(csv.DictReader(file))

    result = []
    for user in users:
        match_id = delete_id and user['Id'] == str(delete_id)
        match_username = delete_username and user['Username'] == delete_username
        if not (match_id or match_username):
            result.append(user)

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(result)


new_user_id = str(unique_id)
new_user_username = input("Print username: ")
new_user_name = input("Print name: ")
new_user_surname = input("Print surname: ")
new_user_email = input("Print email: ")
new_user_phone = str(input("Print phone: "))

new_user = {
    'Id': new_user_id,
    'Username': new_user_username,
    'Name': new_user_name,
    'Surname': new_user_surname,
    'Email': new_user_email,
    'Phone': new_user_phone
}


# add_user(new_user)
# delete_user(delete_id='0088')
# delete_user(delete_username='dfh')
