import requests

from config import BASE_URL, COURIERS_URL
from methods.order_methods import response


class CurierMethod:
    def create_courier(self, login, password, firstName):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}id/')
        return response.text