import requests
from requests.exceptions import JSONDecodeError

import allure


class CourierMethods:

    COURIER_CREATED_MESSAGE = {"ok": True} 

    def __init__(self, url):
        self.url = url

    @allure.step("Create a courier")
    def create(self, payload=None, headers=None):
        response = requests.post(
            url=self.url,
            data=payload
        )
        return response

    @staticmethod
    def get_status_code(response):
        return response.status_code
    
    @staticmethod
    def deserialize(response):
        try:
            return response.json()
        except JSONDecodeError:
            return None
