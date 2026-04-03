import allure


from methods.base_methods import Methods


@allure.suite('The methods of order API')
class OrderMethods(Methods):

    def __init__(self, url):
        self.url = url

    @allure.step('Create an order with data:{payload}, headers:{headers}')
    def create(self, payload, headers=None):
        return self.post(self.url, data=payload, headers=headers)
