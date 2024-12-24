import allure
from conftest import courier_and_login, order_id
from methods.order_methods import OrderMethods
from config import ORDER_DATA, COURIER_RESPONSES

@allure.feature("Заказы")
class TestOrders:
    @allure.title("Тест на проверку получения списка заказов по ID курьера")
    def test_get_orders_success(self, courier_and_login, order_id):
        courier_id = courier_and_login
        order_methods = order_id["order_methods"]
        created_order_id = order_id["order_id"]
        accept_order_response = order_methods.accept_order(created_order_id, courier_id)
        get_orders_response = order_methods.get_orders(courier_id=courier_id)
        response_json = get_orders_response.json()
        assert accept_order_response.status_code == 200 and isinstance(response_json.get("orders"), list), (
            f"'orders' is not a list or missing: {response_json}"
        )

    @allure.title("Успешное получение заказа по трекинговому номеру")
    def test_get_order_by_track_success(self):
        order_methods = OrderMethods()
        create_order_response = order_methods.create_order(ORDER_DATA["order_data_black"])
        track_number = create_order_response.json().get("track")
        get_order_response = order_methods.get_order_by_track(track_number)
        response_json = get_order_response.json()
        assert get_order_response.status_code == 200 and "order" in response_json, (
            f"Expected status 200 with 'order' in response, but got {get_order_response.status_code} and {response_json}"
        )

    @allure.title("Запрос с несуществующим номером заказа возвращает ошибку")
    def test_get_order_by_track_nonexistent_number(self):
        order_methods = OrderMethods()
        nonexistent_track_number = 99999999
        response = order_methods.get_order_by_track(nonexistent_track_number)
        response_json = response.json()
        assert response.status_code == 404 and response_json.get("message") == COURIER_RESPONSES["not_found_number_order"], (
            f"Expected status 404 with message '{COURIER_RESPONSES['not_found_number_order']}', "
            f"but got {response.status_code} and {response_json}"
        )

    @allure.title("Запрос без номера заказа возвращает ошибку")
    def test_get_order_by_track_missing_number(self):
        order_methods = OrderMethods()
        response = order_methods.get_order_by_track("")
        response_json = response.json()
        assert response.status_code == 400 and response_json.get("message") == COURIER_RESPONSES["not_found_data"], (
            f"Expected status 400 with message '{COURIER_RESPONSES['not_found_data']}', "
            f"but got {response.status_code} and {response_json}"
        )
