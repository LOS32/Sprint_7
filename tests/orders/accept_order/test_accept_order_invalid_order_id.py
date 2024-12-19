import allure
from config import INVALID_ORDER_ID, COURIER_RESPONSES
from conftest import courier_and_login, order

@allure.feature("Принятие заказа")
class TestAcceptOrderMissingCourierId:
    @allure.title("Попытка принять заказ с некорректным ID заказа")
    def test_accept_order_invalid_order_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        invalid_order_id = INVALID_ORDER_ID
        courier_id = courier_and_login
        accept_order_response = order_methods.accept_order(invalid_order_id, courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["order_not_found"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['order_not_found']}', "
            f"but got {accept_order_response.status_code} and {response_json}"
        )