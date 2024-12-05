from unittest.mock import patch
import pytest
from Sprint_7.data import ORDER_DATA_1, ORDER_DATA_2
from methods.order_methods import response


class TestCreateOrder:
    def test_create_order(self, courier.order_methods):
        status_code, response_cobtext = order_methods.post_order(courier.id)
        assert status_code == '201' and response_cobtext, (
            f'Status is {status_code} == 201, context is {response_cobtext} == "\{"ok": "true"}"'
        )

    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_1,
            ORDER_DATA_2,
        ]
    )
    def test_check_track_id(self, courier, order_data, order_methods):
        response_order = order_methods.post_order(courier.id, order_methods)
        assert response_order[0] == 400