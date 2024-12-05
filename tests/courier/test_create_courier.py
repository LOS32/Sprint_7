from Sprint_7.methods.courier_methods import CourierMethods
from Sprint_7.data import COURIER_DATA

class TestCourier:
    def test_create_courier(self):
        courier_data = COURIER_DATA["valid_courier"]
        response = CourierMethods().create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["firstName"]
        )
        status_code = response.status_code
        response_text = response.json().get("ok")
        assert status_code == 201 and response_text, (
            f"Status is {status_code} == 201, context is {response_text} == '{{\"ok\": \"true\"}}'"
        )

