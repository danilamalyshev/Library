import csv
import logging
from utils import generate_unique_user_id
from utils import check_username

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def add_user(generate_id, check_uname):
    field_names = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone','Password','Administrator']

    with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    new_user = {
        'Id': generate_id,
        'Username': check_uname,
        'Name': input("Print name: "),
        'Surname': input("Print surname: "),
        'Email': input("Print email: "),
        'Phone': str(input("Print phone: ")),
        'Password': input("Print password: "),
        'Administrator': 'No'
    }
    reader.append(new_user)

    with open('../DATABASE/customer.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(reader)


def delete_user(delete_id=None, delete_username=None):
    headers = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone']

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

del_id = '1241'
del_uname = 'dfh'
add_user(generate_id=generate_unique_user_id(), check_uname=check_username())
# delete_user(delete_id=del_id)
# delete_user(delete_username=del_uname)