import pytest

import data
from methods.courier import CourierMethods 


@pytest.fixture(scope='function')
def courier():
    return data.Courier()


@pytest.fixture(scope='function')
def existed_courier_data(courier):
    payload = courier.payload
    CourierMethods(
        url=data.BASE_URL+data.COURIER_HANDLER
    ).create(payload=payload)

    return payload

