from http import HTTPStatus

import allure
import pytest

import data
from methods.courier import CourierMethods


@allure.suite("Test Courier API: create and etc")
class TestCourierAPI:

    @allure.title('Create a courier with expected data')
    @allure.description('The login, password and fist name are expected')
    def test_create_courier_with_expected_data(self, courier):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER
        ).create(payload=courier.payload)

        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.CREATED
            and
            CourierMethods.deserialize(response) ==
            CourierMethods.COURIER_CREATED_MESSAGE
        ), (
            f"Data {courier.payload} {response.text}"
        )

    @allure.title('Create a courier with ununique courier data')
    @allure.description('The login, password and fist name are '
                        'had an existed courier')
    def test_create_courier_with_ununique_data(self, existed_courier_data):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER
        ).create(payload=existed_courier_data)
        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.CONFLICT
            and
            CourierMethods.deserialize(response).get('message') ==
            CourierMethods.COURIER_CREATED_MESSAGE_WITH_CONFLICT.get(
                'message'
            )
        ), (
            f"Data {existed_courier_data} {response.text}"
        )

    @allure.title('Create a courier without fist name')
    @allure.description('The login, password are expected only. '
                        'Creating a courier is allowed')
    def test_create_courier_without_first_name_is_allowed(self, courier):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER
        ).create(payload=courier.payload_without_first_name)

        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.CREATED and
            CourierMethods.deserialize(response) ==
            CourierMethods.COURIER_CREATED_MESSAGE
        ), (
            f"Data {courier.payload} {response.text}"
        )

    @allure.title('Create a courier without login or password')
    @allure.description('Creating a courier without login '
                        'or password is not allowed')
    @pytest.mark.parametrize(
        'payload', [data.courier.payload_without_login,
                    data.courier.payload_without_password,
                    data.courier.payload_without_login_and_password])
    def test_create_courier_without_login_or_password_is_not_allowed(
        self, payload
    ):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER
        ).create(payload=payload)
        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.BAD_REQUEST
            and
            CourierMethods.deserialize(response).get('message') ==
            CourierMethods.COURIER_CREATED_MESSAGE_WITH_BAD_REQUEST.get(
                'message'
            )
        ), (
            f"Data {payload} {response.text}"
        )
