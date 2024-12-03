from selenium.webdriver.common.by import By


class MainPage:
    mn_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")  # кнопка личный кабинет
    mn_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка войти в аккаунт
    mn_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    mn_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    mn_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    mn_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    mn_h_sauces = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"

    mn_ban_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    mn_h_ban = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"

    mn_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    mn_h_filling = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"


class AuthLogin:
    al_login_text = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок страницы входа
    al_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")  # ссылка на страницу входа
    al_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")  # Кнопка входа
    al_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")  #
    al_email_field = (
        By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # поле ввода почты
    al_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # полу ввода пароля


class AuthRegistration:
    ar_name_field = (By.XPATH,
                     ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")  # поле ввода имени при регистрации
    ar_email_field = (By.XPATH,
                      ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")  # поле ввода почты при регистрации
    ar_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")  # поле ввода пароля при регистрации
    ar_register_button = (
        By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться при регистрации
    ar_error_message = (
        By.XPATH, ".//p[contains(@class, 'input__error')]")  # сообщение об ошибке Такой пользователь уже существует
    ar_error_message_2 = (
        By.XPATH,
        ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")  # сообщение об ошибке
    ar_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")  # ссылка на страницу входа


class AuthPassword:
    ap_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")  # ссылка на страницу входа


class LKProfile:
    lk_logout_button = (By.XPATH, ".//button[text()='Выход']")  # кнопка Выход в Личном Кабинете
    lk_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")  # сообщение Персональные данные
    lk_history_shop_button = (By.XPATH,
                              ".//li[@class='Account_listItem__35dAP']/" \
                              "a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    # кнопка История заказов в личном кабинете
    h1_tag = (By.XPATH, ".//h1")