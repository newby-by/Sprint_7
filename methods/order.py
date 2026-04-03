import allure

from methods.base_methods import Methods


@allure.suite('The methods of order API')
class OrderMethods(Methods):

    @allure.step('Create an order with data:{payload}, headers:{headers}')
    def create(self, payload, headers=None):
        return self.post(data=payload, headers=headers)

    @allure.step('Get a list of orders')
    def get_orders(self, headers=None):
        return self.get(headers=headers)
