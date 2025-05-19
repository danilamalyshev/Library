import csv
import logging
import random

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='../DATABASE/app.log',
#     filemode='w'
# )

def generate_id():
    def gen_id():
        return ''.join(random.choices('0123456789', k=4))


    def save_users_ids():
        existing_ids = set()
        try:
            with open('../Bookstore/customer.csv', mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    existing_ids.add(row['Id'])
        except FileNotFoundError:
            logging.warning(f"File {'../DATABSE/app.log'} not found.")
        return existing_ids


    def generate_unique_user_id():
        existing_ids = save_users_ids()
        attempt = 0

        while attempt < 10000:
            new_id = gen_id()
            if new_id not in existing_ids:
                return new_id
            attempt += 1
    return generate_unique_user_id()

def check_username():
    def save_usernames():
        existing_usernames = set()
        try:
            with open('Bookstore/customer.csv', mode='r', encoding='utf-8') as file:
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
