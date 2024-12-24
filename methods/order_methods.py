import requests
import allure
from config import BASE_URL, ORDERS_URL

class OrderMethods:
    @allure.step("Завершение заказа")
    def post_order(self, id, params):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}finish/{id}", json=params)
        return response.status_code, response.json()

    @allure.step("Удаление заказа")
    def delete_order(self, id, params):
        response = requests.delete(f"{BASE_URL}{ORDERS_URL}delete/{id}", json=params)
        return response.status_code, response.json()

    @allure.step("Создание нового заказа")
    def create_order(self, order_data):
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=order_data)
        return response

    @allure.step("Получение списка заказов для курьера")
    def get_orders(self, courier_id=None):
        params = {}
        if courier_id:
            params["courierId"] = courier_id
        response = requests.get(f"{BASE_URL}{ORDERS_URL}", params=params)
        return response

    @allure.step("Принятие заказа курьером")
    def accept_order(self, order_id, courier_id):
        response = requests.put(f"{BASE_URL}{ORDERS_URL}accept/{order_id}?courierId={courier_id}")
        return response

    @allure.step("Получение информации о заказе по трек-номеру")
    def get_order_by_track(self, track_number):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}/track", params={"t": track_number})
        return response

