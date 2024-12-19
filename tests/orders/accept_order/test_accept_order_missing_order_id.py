import allure
from config import NO_ORDER_ID, COURIER_RESPONSES
from conftest import courier_and_login, order

@allure.feature("Принятие заказа")
class TestAcceptOrderMissingOrderId:
    @allure.title("Попытка принять заказ без ID заказа")
    def test_accept_order_missing_order_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        courier_id = courier_and_login
        no_order_id = NO_ORDER_ID
        accept_order_response = order_methods.accept_order(no_order_id, courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["not_found_generic"]