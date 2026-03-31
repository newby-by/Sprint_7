import pytest

import data


@pytest.fixture(scope='function')
def courier_data():
    return data.Courier()
