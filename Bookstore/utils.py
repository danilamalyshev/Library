import random

def generate_id():
    return ''.join(random.choices('0123456789', k=4))
