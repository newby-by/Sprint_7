import json
from abc import ABC

import requests
from requests.exceptions import JSONDecodeError


class Methods(ABC):

    def __init__(self, url):
        self.url = url

    def post(self, *, data=None, headers=None):
        headers = dict() if headers is None else headers
        headers |= {'Content-Type': 'application/json'}
        return requests.post(
            url=self.url,
            data=json.dumps(data),
            headers=headers
        )

    def get(self, *, headers=None):
        return requests.get(
            url=self.url,
            headers=headers
        )

    def delete(self, *, data=None, headers=None):
        return requests.delete(
            url=self.url,
            data=data,
            headers=headers
        )

    def put(self, *, data=None, headers=None):
        return requests.put(
            url=self.url,
            data=data,
            headers=headers
        )

    @staticmethod
    def get_status_code(response):
        return response.status_code

    @staticmethod
    def deserialize(response):
        try:
            return response.json()
        except JSONDecodeError:
            return None
