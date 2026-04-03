from http import HTTPStatus

import allure
import pytest

import data
from methods.order import OrderMethods


class TestOrder:

    @allure.title('Create an order')
    @allure.description('Creating an order with '
                        'three stats of color {payload}')
    @pytest.mark.parametrize(
        'payload',
        [data.form_data.expected_data,
         data.form_data.expected_data_with_one_color,
         data.form_data.expected_data_with_two_colors,
         data.form_data.expected_data_without_colors]
    )
    def test_create_order(self, payload):
        order_methods = OrderMethods(url=data.BASE_URL+data.ORDER_HANDLER)
        response = order_methods.create(payload=payload)
        assert (response.status_code == HTTPStatus.CREATED and
                'track' in OrderMethods.deserialize(response))

    @allure.title('Get a list of order')
    @allure.description('Getting all list, without query params')
    def test_get_list_orders(self):
        order_methods = OrderMethods(url=data.BASE_URL+data.ORDER_HANDLER)
        response = order_methods.get_orders()
        assert (response.status_code == HTTPStatus.OK and
                isinstance(
                    OrderMethods.deserialize(response).get("orders"), list
                ))
