import requests
from config import BASE_URL, ORDERS_URL

class OrderMethods:
    def post_order(self, id, params):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}finish/{id}", json=params)
        return response.status_code, response.json()

    def delete_order(self, id, params):
        response = requests.delete(f"{BASE_URL}{ORDERS_URL}delete/{id}", json=params)
        return response.status_code, response.json()

    def create_order(self, order_data):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=order_data)
        return response

    def get_orders(self, courier_id=None):
        params = {}
        if courier_id:
            params["courierId"] = courier_id
        response = requests.get(f"{BASE_URL}{ORDERS_URL}", params=params)
        return response

    def accept_order(self, order_id, courier_id):
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/{order_id}?courierId={courier_id}")
        return response

    def get_order_by_track(self, track_number):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}/track", params={"t": track_number})
        return response

