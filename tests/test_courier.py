from http import HTTPStatus

import allure

import data
from methods.courier import CourierMethods


@allure.suite("Test Courier API: create and etc")
class TestCourierAPI:

    @allure.title('Create a courier with expected data')
    @allure.description('The login, password and fist name are expected')
    def test_create_courier_with_expected_data(self, courier_data):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER
        ).create(payload=courier_data.payload)

        assert CourierMethods.get_status_code(response) == HTTPStatus.CREATED
