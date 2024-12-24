import allure
from config import (
    NO_ORDER_ID,
    NO_COURIER_ID,
    INVALID_ORDER_ID,
    INVALID_COURIER_ID,
    COURIER_RESPONSES
)
from conftest import courier_and_login, order


@allure.feature("Принятие заказа")
class TestAcceptOrder:
    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, courier_and_login, order):
        order_methods = order["order_methods"]
        courier_id = courier_and_login
        order_track = order["order_track"]
        get_order_response = order_methods.get_order_by_track(order_track)
        id_order = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(id_order, courier_id)
        assert accept_order_response.status_code == 200 and accept_order_response.json().get("ok") is True, (
            f"Expected status 200 with 'ok': true, but got {accept_order_response.status_code} and {accept_order_response.json()}"
        )

    @allure.title("Попытка принять заказ без ID заказа")
    def test_accept_order_missing_order_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        courier_id = courier_and_login
        accept_order_response = order_methods.accept_order(NO_ORDER_ID, courier_id)
        assert accept_order_response.status_code == 404 and accept_order_response.json().get("message") == COURIER_RESPONSES["not_found_generic"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['not_found_generic']}', "
            f"but got {accept_order_response.status_code} and {accept_order_response.json()}"
        )

    @allure.title("Попытка принять заказ без ID курьера")
    def test_accept_order_missing_courier_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        order_track = order["order_track"]
        get_order_response = order_methods.get_order_by_track(order_track)
        id_order = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(id_order, NO_COURIER_ID)
        assert accept_order_response.status_code == 400 and accept_order_response.json().get("message") == COURIER_RESPONSES["not_found_data"], (
            f"Expected status 400 with message '{COURIER_RESPONSES['not_found_data']}', "
            f"but got {accept_order_response.status_code} and {accept_order_response.json()}"
        )

    @allure.title("Попытка принять заказ с некорректным ID заказа")
    def test_accept_order_invalid_order_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        courier_id = courier_and_login
        accept_order_response = order_methods.accept_order(INVALID_ORDER_ID, courier_id)
        assert accept_order_response.status_code == 404 and accept_order_response.json().get("message") == COURIER_RESPONSES["order_not_found"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['order_not_found']}', "
            f"but got {accept_order_response.status_code} and {accept_order_response.json()}"
        )

    @allure.title("Попытка принять заказ с неверным ID курьера")
    def test_accept_order_invalid_courier_id(self, courier_and_login, order):
        order_methods = order["order_methods"]
        order_track = order["order_track"]
        get_order_response = order_methods.get_order_by_track(order_track)
        id_order = get_order_response.json()["order"].get("id")
        accept_order_response = order_methods.accept_order(id_order, INVALID_COURIER_ID)
        assert accept_order_response.status_code == 404 and accept_order_response.json().get("message") == COURIER_RESPONSES["courier_id_not_found"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['courier_id_not_found']}', "
            f"but got {accept_order_response.status_code} and {accept_order_response.json()}"
        )
