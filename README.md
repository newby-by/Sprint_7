# The project collects some api tests

We use Scooter app, [see more](http://qa-scooter.praktikum-services.ru/).

## Acknowledgments

The Praktikum team

My Tomcat that get me up early.
Your 4 a.m. song is so cool.

## How we test

### Create a courier

1. A courier is created with expected data: `login`, `password` and `firstName`.

[See the test](./tests/test_courier.py#test_create_courier_with_expected_data)

Test in command line

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c","password":"lkncx8y&^5vgg","firstName":"Alice"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

```

**Response**

```bash
{"ok":true}
```

**Note** You should use `login`, `password` and `firstName` with other data.

2. Creating a courier with existent login is not allowed.

[See the test](./tests/test_courier.py#test_create_courier_with_ununique_data)

Test in command line

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c3452","password":"lkncx8y&^5vgg","firstName":"Alice"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c3452","password":"lkncx8y&^5vgg","firstName":"Alice"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

```

**Response**
*TODO CHECK MESSAGE* `. Попробуйте другой`.

```bash
HTTP/1.1 409 Сonflict
{
    "message": "Этот логин уже используется. Попробуйте другой."
}
```

3. Create a courier without fist name, it is allowed.

[See the test](./tests/test_courier.py#test_create_courier_without_first_name_is_allowed)

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c12","password":"lkncx8y&^5vgg"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

```

**Response**

```bash
{"ok":true}
```

4. Creating a courier without login or password is not allowed.

[See the test](./tests/test_courier.py#test_create_courier_without_first_name_is_allowed)

```bash without login
curl POST -H "Content-Type:Application/json" \
-d '{"password":"lkncx8y&^5vgg","firstName":"Alice"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

```

```bash without password
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c12","firstName":"Alice"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier

```

**Response**

```bash
{"code":400,"message":"Недостаточно данных для создания учетной записи"}
```

### Login a courier

1. An existent courier can set in with expected data, the response data has `id` courier.

[See the test](./tests/test_login_courier.py#test_login_courier_with_expected_data)

Test in command line

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c","password":"lkncx8y&^5vgg"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier/login

```

**Response**

```bash
{"id":726462}
```

2. Set in with a wrong login or password, the response has an error.

[See the test](./tests/test_login_courier.py#test_login_courier_with_expected_data)

Test in command line with a wrong login `d3jh7c1`

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c1","password":"lkncx8y&^5vgg"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier/login

```

**Response**

```bash
{"code":404,"message":"Учетная запись не найдена"}
```

Test in command line with a wrong password `lkncx8y&^5vgg1`

```bash
curl POST -H "Content-Type:Application/json" \
-d '{"login":"d3jh7c","password":"lkncx8y&^5vgg1"}' \
https://qa-scooter.praktikum-services.ru/api/v1/courier/login

```

**Response**

```bash
{"code":404,"message":"Учетная запись не найдена"}

2. Set in without a login or a password, the response has an error.

Test in command line without a login

```bash
 curl POST -H "Content-Type:Application/json" -d '{"password":"lkncx8y&^5vgg"}' https://qa-scooter.praktikum-services.ru/api/v1/courier/login
```

**Response**

```bash
{"code":400,"message":"Недостаточно данных для входа"}
```

### Create an order

1. Create an order with color BLACK or GREY.

```bash
 curl POST -H "Content-Type:Application/json" -d '{"firstName":"Naruto","lastName":"Uchiha","address":"Konoha, 142 apt.","metroStation":4,"phone":"+7 800 355 35 35","rentTime":5,"deliveryDate":"2020-06-06","comment":"Saske, come back to Konoha","color":["BLACK"]}' https://qa-scooter.praktikum-services.ru/api/v1/orders
```

**Response**

```bash
{"track":656114}
```

2. Create an order with color BLACK and GREY.

```bash
 curl POST -H "Content-Type:Application/json" -d '{"firstName":"Naruto","lastName":"Uchiha","address":"Konoha, 142 apt.","metroStation":4,"phone":"+7 800 355 35 35","rentTime":5,"deliveryDate":"2020-06-06","comment":"Saske, come back to Konoha","color":["BLACK", "GREY"]}' https://qa-scooter.praktikum-services.ru/api/v1/orders
```

**Response**

```bash
{"track":656119}
```

3. Create an order without color.

```bash
 curl POST -H "Content-Type:Application/json" -d '{"firstName":"Naruto","lastName":"Uchiha","address":"Konoha, 142 apt.","metroStation":4,"phone":"+7 800 355 35 35","rentTime":5,"deliveryDate":"2020-06-06","comment":"Saske, come back to Konoha"}' https://qa-scooter.praktikum-services.ru/api/v1/orders
```

**Response**

```bash
{"track":656120}
```
