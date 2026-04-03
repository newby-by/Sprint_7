from http import HTTPStatus

import allure
import pytest

import data
from methods.courier import CourierMethods


@allure.suite("Test Courier API: login")
class TestLoginCourier:


    @allure.title('Login a courier with expected data')
    @allure.description('The login and password are expected')
    def test_login_courier_with_expected_data(self, existed_courier):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER+data.COURIER_LOGIN
        ).login(payload=existed_courier.generated_payload_for_login)

        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.OK and
            isinstance(CourierMethods.deserialize(response).get('id'), int)  
        ), (
            f"Data {existed_courier.generated_payload_for_login} {response.text}"
        )

    @allure.title('Login a courier with wrong data')
    @allure.description('The login and password are wrong')
    @pytest.mark.parametrize('method', 
                             [data.Courier.change_login,
                              data.Courier.change_password])
    def test_login_courier_with_wrong_data(self, existed_courier, method):
        method(existed_courier)
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER+data.COURIER_LOGIN
        ).login(payload=existed_courier.generated_payload_for_login)

        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.NOT_FOUND and
            CourierMethods.deserialize(response) == CourierMethods.RESPONSE_LOGIN_COURIER_WITH_WRONG_DATA  
        ), (
            f"Data {existed_courier.generated_payload_for_login} {response.text}"
        )

    @allure.title('Login a courier without required data')
    @allure.description('The login or password are not passed')
    @pytest.mark.parametrize(
        'method',
        [data.Courier.generated_payload_without_login,
         pytest.param(data.Courier.generated_payload_without_password,
                      marks=pytest.mark.xfail(reason='Without a pssword is FAILED'))] 
    )
    def test_login_courier_without_required_data(self, existed_courier, method):
        response = CourierMethods(
            url=data.BASE_URL+data.COURIER_HANDLER+data.COURIER_LOGIN
        ).login(payload=method(existed_courier))

        assert (
            CourierMethods.get_status_code(response) == HTTPStatus.BAD_REQUEST and
            CourierMethods.deserialize(response) == CourierMethods.RESPONSE_LOGIN_COURIER_WITHOUT_REQUIRED_DATA  
        ), (
            f"Data {existed_courier} {response.text}"
        )
