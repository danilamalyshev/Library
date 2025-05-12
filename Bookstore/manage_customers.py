import csv

from Bookstore.utils import generate_id

file_path = '../ DATABASE/customer.csv'

def insert_user(new_user):
    fieldnames = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone']

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    reader.append(new_user)

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)


def delete_user(delete_id=None, delete_username=None):
    fieldnames = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone']

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        customers = list(reader)

    updated_customers = [
        row for row in customers
        if not (
            (delete_id and row['Id'] == str(delete_id)) or
            (delete_username and row['Username'] == delete_username)
        )
    ]

    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_customers)

new_user_id = generate_id()
new_user_username = input("Print username: ")
new_user_name = input("Print name: ")
new_user_surname = input("Print surname: ")
new_user_email = input("Print email: ")
new_user_phone = int(input("Print phone: "))

new_user = {
    'Id': new_user_id,
    'Username': new_user_username,
    'Name': new_user_name,
    'Surname': new_user_surname,
    'Email': new_user_email,
    'Phone': new_user_phone
}

insert_user(new_user)

# insert_user(new_user)
# delete_user(delete_id='6')
# delete_user(delete_username='Neer')