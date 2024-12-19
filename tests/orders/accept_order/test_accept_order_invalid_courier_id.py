import allure
from conftest import courier_and_login, order
from config import INVALID_COURIER_ID, COURIER_RESPONSES

@allure.feature("Принятие заказа")
class TestAcceptOrderInvalidCourierId:
    @allure.title("Попытка принять заказ с неверным ID курьера")
    def test_accept_order_invalid_courier_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        invalid_courier_id = INVALID_COURIER_ID
        order_track = order["order_track"]
        get_order_response = order_methods.get_order_by_track(order_track)
        order_id = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(order_id, invalid_courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["courier_id_not_found"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['courier_id_not_found']}', "
            f"but got {accept_order_response.status_code} and {response_json}"
        )
