import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

config = configparser.ConfigParser()
config.read("../autorization.ini")
autorization = config['YANDEX_LOGIN_PASS']
USERNAME = autorization['username']
PASSWORD = autorization['password']


class TestYandexLogg:

    @pytest.fixture
    def setup_teardown(self):
        self.driver = webdriver.Firefox()
        yield self.driver
        self.driver.close()

    def test_login_to_yandex(self, setup_teardown):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth/")
        driver.find_element(By.ID, "passp-field-login").send_keys(USERNAME)
        driver.find_element(By.ID, "passp:sign-in").click()
        driver.find_element(By.ID, "passp-field-passwd").send_keys(PASSWORD)
        driver.find_element(By.ID, "passp:sign-in").click()
        WebDriverWait(driver, 10).until(ec.url_to_be('https://passport.yandex.ru/profile'))
        assert driver.current_url == 'https://passport.yandex.ru/profile'


if __name__ == '__main__':
    TestYandexLogg.test_login_to_yandex()