import requests
import allure
from config import BASE_URL, COURIERS_URL

class CourierMethods:
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=payload)
        return response

    @staticmethod
    @allure.step("Вход курьера")
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password,
        }
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=payload)
        return response

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{courier_id}')
        if response.status_code == 200:
            print(f"Courier with ID '{courier_id}' successfully deleted.")
        elif response.status_code == 404:
            print(f"Courier with ID '{courier_id}' not found.")
        else:
            print(f"Error deleting courier: {response.status_code}, {response.json()}")
        return response