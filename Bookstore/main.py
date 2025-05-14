from utils import generate_unique_user_id
from manage_customers import add_user

generate_id = generate_unique_user_id()
add_user(generate_id)