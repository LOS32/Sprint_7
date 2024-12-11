from methods.courier_methods import CourierMethods
from config import COURIER_DATA

class TestCannotCreateTwoIdenticalCouriers:
    def test_cannot_create_two_identical_couriers(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(
            COURIER_DATA["valid_courier"]["login"],
            COURIER_DATA["valid_courier"]["password"],
            COURIER_DATA["valid_courier"]["firstName"]
        )
        duplicate_response = courier_methods.create_courier(
            COURIER_DATA["duplicate_courier"]["login"],
            COURIER_DATA["duplicate_courier"]["password"],
            COURIER_DATA["duplicate_courier"]["firstName"]
        )
        assert duplicate_response.status_code == 409 and duplicate_response.json().get("message") == "Этот логин уже используется. Попробуйте другой."

