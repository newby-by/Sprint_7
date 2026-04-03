from datetime import datetime

from faker import Faker


BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER_HANDLER = '/api/v1/courier'
COURIER_LOGIN = '/login'

WRONG_DATA = '1'


class Courier:

    def __init__(self, locale='en_US'):
        self.locale = locale
        self.faker = Faker(locale=self.locale)

    def change_login(self):
        self._login = self._login + WRONG_DATA

    def change_password(self):
        self._password = self._password + WRONG_DATA

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
    def generated_payload(self):
        return {
            "login": self._login,
            "password": self._password,
            "firstName": self._first_name
    
        }

    @property
    def generated_payload_for_login(self):
        return {
            "login": self._login,
            "password": self._password,
        }
    

    def generated_payload_without_login(self):
        return {
            "password": self._password,
        }
    

    def generated_payload_without_password(self):
        return {
            "login": self._login,
        }

    @property
    def payload_without_first_name(self):
        return {
            "login": self.login,
            "password": self.password
        }
    
    @property
    def payload_without_login(self):
        return {
            "password": self.password,
            "firstName": self.first_name
        }

    @property
    def payload_without_password(self):
        return {
            "login": self.login,
            "firstName": self.first_name
        }

    @property
    def payload_without_login_and_password(self):
        return {
            "firstName": self.first_name
        }
    
    def __call__(self):
        return self
    
    def __str__(self):
        return ('{"login": 'f'{self._login},'
                f'"password": {self._password},'
                f'"firstName": {self._first_name}''}')


courier = Courier()


class OrderScooterForm:

    FIELDS = {
        'Имя': 1,
        'Фамилия': 2,
        'Адрес': 3,
        'Станция метро': 4,
        'Телефон': 5,
    }

    RENTAL_PERIOD = {
        'сутки': 1,
        'двое суток': 2,
        'трое суток': 3,
        'четверо суток': 4,
        'пятеро суток': 5,
        'шестеро суток': 6,
        'семеро суток': 7,
    }

    SCOOTER_COLOR = {
        'чёрный жемчуг': 1,
        'серая безысходность': 2,
    }

    def __init__(self):
        self.template_data = {
            'Имя': None,
            'Фамилия': None,
            'Адрес': None,
            'Станция метро': None,
            'Телефон': None,
            'Дата доставки': None,
            'Срок аренды': None,
            'Цвет': None,
            'Комментарий': None,
        }


class OrderScooterData:

    def __init__(self, locale='ru_RU'):
        self.template_data = OrderScooterForm().template_data
        self.faker = Faker(locale)

    @property
    def first_name(self):
        return self.faker.first_name()

    @property
    def last_name(self):
        return self.faker.last_name()

    @property
    def address(self):
        return self.faker.address()[:49].replace('/', '')

    @property
    def metro(self):
        return 'Черкизовская'

    @property
    def phone_number(self):
        return self.faker.numerify("89#########")

    @property
    def date_of_pick_up(self):
        pattern = "%d.%m.%Y"

        start_date = datetime.now()
        end_date = datetime(2026, 12, 31)

        random_date = self.faker.date_between_dates(
            date_start=start_date,
            date_end=end_date
        )

        return random_date.strftime(pattern)

    @property
    def rental_period(self):
        periods = list(OrderScooterForm.RENTAL_PERIOD)
        return self.faker.random_element(elements=periods)

    @property
    def scooter_color(self):
        colors = list(OrderScooterForm.SCOOTER_COLOR)
        return self.faker.random_element(elements=colors)

    @property
    def comments_for_courier(self):
        return self.faker.sentence()

    @property
    def expected_data(self):
        self.template_data['Имя'] = self.first_name
        self.template_data['Фамилия'] = self.last_name
        self.template_data['Адрес'] = self.address
        self.template_data['Станция метро'] = self.metro
        self.template_data['Телефон'] = self.phone_number
        self.template_data['Дата доставки'] = self.date_of_pick_up
        self.template_data['Срок аренды'] = self.rental_period
        self.template_data['Цвет'] = self.scooter_color
        self.template_data['Комментарий'] = self.comments_for_courier
        return self.template_data

    def __str__(self):
        return str(self.template_data)


form_data = OrderScooterData()
