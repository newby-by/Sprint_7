import allure
import requests

from methods.base_methods import Methods


class CourierMethods(Methods):

    COURIER_CREATED_MESSAGE = {"ok": True}
    COURIER_CREATED_MESSAGE_WITH_CONFLICT = {
        "message": "Этот логин уже используется. Попробуйте другой."
    }
    COURIER_CREATED_MESSAGE_WITH_BAD_REQUEST = {
        "message": "Недостаточно данных для создания учетной записи"
    }

    RESPONSE_LOGIN_COURIER_WITH_WRONG_DATA = {
        "code": 404,
        "message": "Учетная запись не найдена"
    }
    RESPONSE_LOGIN_COURIER_WITHOUT_REQUIRED_DATA = {
        "code": 400,
        "message": "Недостаточно данных для входа"
    }

    @allure.step("Create a courier")
    def create(self, payload=None, headers=None):
        response = self.post(data=payload)
        return response

    @allure.step("Login a courier")
    def login(self, payload=None):
        return self.post(data=payload)
