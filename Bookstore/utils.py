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
        new_id = generate_id()

        if new_id not in existing_ids:
            return new_id
        attempt += 1






unique_id = generate_unique_user_id()