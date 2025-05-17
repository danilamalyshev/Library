import csv
import logging
from utils import generate_id

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def add_user(generate_id):
    field_names = ['Id', 'Username', 'Name', 'Surname', 'Email', 'Phone','Password','Administrator']

    with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))

    def check_username():
        def save_usernames():
            existing_usernames = set()
            try:
                with open('../DATABASE/customer.csv', mode='r', encoding='utf-8') as file:
                    reader = list(csv.DictReader(file))
                    for row in reader:
                        existing_usernames.add(row['Username'])
            except FileNotFoundError:
                logging.warning(f"File {'../DATABASE/customer.csv'} not found.MC")
            return existing_usernames

        def check_username_in_file():
            existing_usernames = save_usernames()

            while True:
                username = input("Enter username: ")
                if username in existing_usernames:
                    print("This username is already registered, try again.")
                else:
                    return username

        return check_username_in_file()

    new_user = {
        'Id': generate_id,
        'Username': check_username(),
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


def delete_user(delete_id, delete_username):
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
add_user(generate_id=generate_id())
# delete_user(delete_id=del_id)
# delete_user(delete_username=del_uname)