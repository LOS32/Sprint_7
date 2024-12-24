import pytest
from config import ORDER_DATA
from conftest import order

class TestCreateOrder:
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA["order_data_black"],
            ORDER_DATA["order_data_grey"],
            ORDER_DATA["order_data_no_color"],
            ORDER_DATA["order_data_two_colors"]
        ]
    )
    def test_create_order(self, order, order_data):
        response = order["order_methods"].create_order(order_data)
        response_json = response.json()
        assert response.status_code == 201 and "track" in response_json, \
            f"Expected status 201 and 'track' in response, got {response.status_code} and {response_json}"






