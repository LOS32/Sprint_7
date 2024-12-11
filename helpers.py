import random
import string
import uuid


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    def generate_random_password(length):
        digits = string.digits
        return ''.join(random.choice(digits) for i in range(length))

    login = generate_random_string(5)  # Добавляем уникальную часть
    password = generate_random_password(4)
    first_name = generate_random_string(5)

    return [login, password, first_name]




