import random
import csv

file_path_user = '../ DATABASE/customer.csv'

def generate_id():
    return ''.join(random.choices('0123456789', k=4))

new_id = '1091'
def save_users_ids():
    existing_ids = set()
    try:
        with open(file_path_user, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_ids.add(row['Id'])
    except FileNotFoundError:
        pass
    return existing_ids

def generate_unique_user_id(new_id):
    existing_ids = save_users_ids()
    while True:
        if new_id not in existing_ids:
            return new_id

unique_id = generate_unique_user_id(new_id)

