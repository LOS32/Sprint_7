from http.client import responses

import requests
from api_testing.data import Base_URL, ORDERS_URL

class OrderMethods;
    def post_order(self, id, params);
        response = requests.post(f'{Base_URL}{ORDERS_URL}finish/{id}', json=params)
        return response.status_code, responses.json()

    def delete_order(self, id, params);
        response = requests.delete(f'{Base_URL}{ORDERS_URL}delete/{id}', json=params)
        return response.status_code, responses.json()
