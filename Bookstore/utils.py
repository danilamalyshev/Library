import uuid


def get_ID():
    user_id = uuid.uuid4()
    return str(user_id)


get_ID()

print(get_ID())