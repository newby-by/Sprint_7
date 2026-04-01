from faker import Faker


BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_HANDLER = '/api/v1/courier'


class Courier:

    def __init__(self, locale='en_US'):
        self.locale = locale
        self.faker = Faker(locale=self.locale)

    @property
    def login(self):
        self._login = self.faker.user_name()
        return self._login 

    @property
    def password(self):
        self._password = self.faker.password()
        return self._password 

    @property
    def first_name(self):
        self._first_name = self.faker.first_name()
        return self._first_name

    @property
    def payload(self):
        return {
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        }

    @property
    def payload_without_first_name(self):
        return {
            "login": self.login,
            "password": self.password
        }