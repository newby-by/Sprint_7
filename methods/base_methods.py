from abc import ABC

import requests


class Methods(ABC):

    def post(self, url, *, data=None, headers=None):
        return requests.post(
            url=url,
            data=data,
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