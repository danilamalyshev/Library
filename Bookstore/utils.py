import random

def generate_id():
    return ''.join(random.choices('0123456789', k=4))

new_id = generate_id()
print(new_id)