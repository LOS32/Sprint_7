import allure
from conftest import courier_and_login, order

@allure.feature("Принятие заказа")
class TestAcceptOrderSuccess:
    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, courier_and_login, order):
        order_methods = order["order_methods"]
        courier_id = courier_and_login
        order_track = order["order_track"]
        get_order_response = order_methods.get_order_by_track(order_track)
        order_id = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(order_id, courier_id)
        response_json = accept_order_response.json()
        assert accept_order_response.status_code == 200 and response_json.get("ok") is True, (
            f"Expected status 200 with 'ok': true, but got {accept_order_response.status_code} and {response_json}"
        )






