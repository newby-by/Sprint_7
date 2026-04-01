# The project collects some api tests

We use Scooter app, [see more](http://qa-scooter.praktikum-services.ru/).

## Acknowledgments

The Praktikum team

My Tomcat that get me up early.
Your 4 a.m. song is so cool.

## How we test

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

5. Creating a courier with existed login is not allowed.
