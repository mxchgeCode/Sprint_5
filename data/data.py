from faker import Faker


class PersonData:
    user_name = 'Иван Иванов'
    login = 'ivanivanov@eda.ru'
    password = 'KeyboardInterrupt123'


class ValidData:
    fake = Faker()
    user_name = fake.name_male()
    login = fake.email()
    password = fake.password()
