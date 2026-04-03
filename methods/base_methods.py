import json
from abc import ABC

import requests
from requests.exceptions import JSONDecodeError

class Methods(ABC):

    def post(self, url, *, data=None, headers=None):
        headers = dict() if headers is None else headers
        headers |= {'Content-Type': 'application/json'}
        return requests.post(
            url=url,
            data=json.dumps(data),
            headers=headers
        )

    def get(self, url, *, headers=None):
        return requests.get(
            url=url,
            headers=headers
        )

    def delete(self, url, *, data=None, headers=None):
        return requests.delete(
            url=url,
            data=data,
            headers=headers
        )

    def put(self, url, *, data=None, headers=None):
        return requests.put(
            url=url,
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