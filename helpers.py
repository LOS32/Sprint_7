import random
import string

generated_courier_data = None

def register_new_courier_and_return_login_password():
    global generated_courier_data
    if generated_courier_data is None:
        def generate_random_string(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
        def generate_random_password(length):
            digits = string.digits
            return ''.join(random.choice(digits) for i in range(length))
        login = generate_random_string(5)
        password = generate_random_password(4)
        first_name = generate_random_string(5)
        generated_courier_data = [login, password, first_name]
    return generated_courier_data





