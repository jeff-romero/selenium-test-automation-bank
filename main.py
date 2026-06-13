from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import inspect
from constants import *

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


def load_home_page():
    driver.get(HOME_PAGE)


class TestLogin:
    def __init__(self):
        pass

    def test_invalid_username(self):
        try:
            load_home_page()

            WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
                expected_conditions.presence_of_element_located((By.XPATH, USERNAME_INPUT))
            )

            username_input = driver.find_element(By.XPATH, USERNAME_INPUT)
            username_input.clear()
            username_input.send_keys("asd123" + Keys.ENTER)

            WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[@class='error']"), "Please enter a username and password.")
            )
        except Exception as e:
            print(f"{inspect.stack()[0][3]}: {e}")
        else:
            print(f"{inspect.stack()[0][3]}: PASS")

    def test_invalid_password(self):
        try:
            load_home_page()

            WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
                expected_conditions.presence_of_element_located((By.XPATH, PASSWORD_INPUT))
            )

            password_input = driver.find_element(By.XPATH, PASSWORD_INPUT)
            password_input.clear()
            password_input.send_keys("zxc456" + Keys.ENTER)

            WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[@class='error']"), "Please enter a username and password.")
            )
        except Exception as e:
            print(f"{inspect.stack()[0][3]}: {e}")
        else:
            print(f"{inspect.stack()[0][3]}: PASS")


if __name__ == "__main__":
    test_login = TestLogin()
    test_login.test_invalid_username()
    test_login.test_invalid_password()
    driver.quit()
