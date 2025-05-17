import csv
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

file_path_user = '../DATABASE/customer.csv'


def generate_id():
    gen_id()
    save_users_ids()
    generate_unique_user_id()


def gen_id():
    return ''.join(random.choices('0123456789', k=4))


def save_users_ids():
    existing_ids = set()
    try:
        with open(file_path_user, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_ids.add(row['Id'])
    except FileNotFoundError:
        logging.warning(f"File {file_path_user} not found.")
    return existing_ids


def generate_unique_user_id():
    existing_ids = save_users_ids()
    attempt = 0

    while attempt < 10000:
        new_id = gen_id()
        if new_id not in existing_ids:
            return new_id
        attempt += 1


def user_login():
    while True:
        print('If you want to leave, type "exit"')
        username = input('Enter username: ')
        if username.lower() == 'exit':
            break

        with open(file_path_user, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            user_found = False

            for row in reader:
                if row['Username'] == username:
                    user_found = True
                    password = input('Enter password: ')
                    if password == 'exit':
                        return
                    if password == row['Password']:
                        if row['Administrator'] == 'Yes':
                            admin_login = input('Login as admin?(yes/no): ')
                            if admin_login == 'yes':
                                print('Welcome admin ' + row['Username'])
                                print('You can manage customers and books:')
                                print('Add user')
                                return
                            else:
                                print('Welcome ' + row['Username'])
                                return
                    else:
                        print('Wrong password')
                        break

            if not user_found:
                print('Invalid username')


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
