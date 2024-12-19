import allure
from conftest import courier_and_login, order_id

@allure.feature("Получение списка заказов")
class TestGetOrders:
    @allure.title("Тест на проверку получения списка заказов по ID курьера")
    def test_get_orders(self, courier_and_login, order_id):
        courier_id = courier_and_login
        order_methods = order_id["order_methods"]
        created_order_id = order_id["order_id"]
        accept_order_response = order_methods.accept_order(created_order_id, courier_id)
        get_orders_response = order_methods.get_orders(courier_id=courier_id)
        response_json = get_orders_response.json()
        assert accept_order_response.status_code == 200 and isinstance(response_json.get("orders"), list), f"'orders' is not a list or missing: {response_json}"



