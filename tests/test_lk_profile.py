from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.pages import Pages
from web_locators.locators import *


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login, driver):
        """ Переход в личный кабинет """

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        profile = driver.find_element(*LKProfile.lk_history_shop_button)
        assert Pages.url_profile == driver.current_url and profile.text == 'История заказов'

    def test_click_constructor_button_show_constructor_form(self, login, driver):
        """ Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор' """

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        driver.find_element(*MainPage.mn_constructor_button).click()

        h1_tag = driver.find_elements(*LKProfile.h1_tag)
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login, driver):
        """ Переход из личного кабинета в конструктор при нажатии на лого """

        driver.find_element(*MainPage.mn_profile_button).click()

        WebDriverWait(driver, 3).until(EC.presence_of_element_located(LKProfile.lk_info_message))
        driver.find_element(*MainPage.mn_logo).click()

        h1_tag = driver.find_elements(*LKProfile.h1_tag)
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logout_button_in_lk_open_login_form(self, login, driver):
        """ Выход из аккаунта """

        driver.find_element(*MainPage.mn_profile_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LKProfile.lk_info_message))

        driver.find_element(*LKProfile.lk_logout_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthLogin.al_login_button_any_forms))

        login_button = driver.find_element(*AuthLogin.al_login_text)

        assert driver.current_url == Pages.url_login and login_button.text == 'Вход'
