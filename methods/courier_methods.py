import requests
from config import BASE_URL, COURIERS_URL

class CourierMethods:
    def create_courier(self, login, password, firstName):
        payload = {
            "login": login,
            "password": password,
            "firstName": firstName
        }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=payload)
        return response
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=payload)
        return response
    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{courier_id}')
        if response.status_code == 200:
            print(f"Courier with ID '{courier_id}' successfully deleted.")
        elif response.status_code == 404:
            print(f"Courier with ID '{courier_id}' not found.")
        else:
            print(f"Error deleting courier: {response.status_code}, {response.json()}")
        return response