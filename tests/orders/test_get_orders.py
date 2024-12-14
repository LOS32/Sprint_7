import pytest
import allure
from conftest import order

@allure.feature('Список заказов')
class TestGetOrders:
    @allure.title('Тест на проверку получения списка заказов')
    def test_get_orders(self, order):
        # Создаём заказ через фикстуру `order`
        order["order_methods"].create_order(order["order_track"])

        # Получаем список заказов
        response = order["order_methods"].get_orders()
        response_json = response.json()

        # Проверяем, что ключ 'orders' есть в ответе и является списком
        assert isinstance(response_json.get("orders"), list), f"'orders' is not a list or missing: {response_json}"



