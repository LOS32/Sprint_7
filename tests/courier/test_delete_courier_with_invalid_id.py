import allure
from methods.courier_methods import CourierMethods

@allure.feature('Ошибка при удалении курьера')
class TestDeleteCourierWithInvalidId:
@allure.title("Удаление курьера с несуществующим ID")
def test_delete_courier_with_invalid_id():
    courier_methods = CourierMethods()
    invalid_id = 999999  # ID, который точно не существует
    delete_response = courier_methods.delete_courier(invalid_id)
    assert delete_response.status_code == 404 and delete_response.json().get("message") == "Курьера с таким id нет.", (
        f"Expected status 400 with message 'Курьер с таким ID не найден', got "
        f"status {delete_response.status_code} and response {delete_response.json()}"
    )