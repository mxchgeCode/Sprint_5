import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import *
from data.pages import Pages
from data.data import PersonData


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(Pages.url_main_paige)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """ Войти в аккаунт """
    driver.get(Pages.url_login)

    driver.find_element(*AuthLogin.al_email_field).send_keys(PersonData.login)
    driver.find_element(*AuthLogin.al_password_field).send_keys(PersonData.password)
    driver.find_element(*AuthLogin.al_login_button_any_forms).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPage.mn_order_button))
    return driver
