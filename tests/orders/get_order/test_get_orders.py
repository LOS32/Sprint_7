import allure
from conftest import order

@allure.feature('Список заказов')
class TestGetOrders:
    @allure.title('Тест на проверку получения списка заказов')
    def test_get_orders(self, order):
        order["order_methods"].create_order(order["order_track"])
        response = order["order_methods"].get_orders()
        response_json = response.json()
        assert isinstance(response_json.get("orders"), list), f"'orders' is not a list or missing: {response_json}"



