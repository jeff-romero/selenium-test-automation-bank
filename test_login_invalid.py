from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time
import inspect
from constants import *

service = Service(executable_path="chromedriver.exe")


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=service)
    driver.get(HOME_PAGE)
    yield driver
    driver.quit()

def element_present(driver, element):
    try:
        WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
            expected_conditions.presence_of_element_located((By.XPATH, element))
        )
    except Exception as e:
        print(f"{inspect.stack()[0][3]}: Could not find element {element} - {e}")
        return False

    return True

def type_username(driver, username):
    try:
        username_input = driver.find_element(By.XPATH, USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)
    except Exception as e:
        print(f"{inspect.stack()[0][3]}: {e}")
        return False

    return True

def attempt_login_enter_key(driver):
    try:
        username_input = driver.find_element(By.XPATH, USERNAME_INPUT)
        username_input.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"{inspect.stack()[0][3]}: {e}")
        return False

    return True

def type_password(driver, password):
    try:
        password_input = driver.find_element(By.XPATH, PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
    except Exception as e:
        print(f"{inspect.stack()[0][3]}: {e}")
        return False

    return True


def test_invalid_username(driver):
    assert element_present(driver, USERNAME_INPUT) == True

    assert type_username(driver, "asd123") == True

    assert attempt_login_enter_key(driver) == True

    WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[@class='error']"), "Please enter a username and password.")
    )

def test_invalid_password(driver):
    assert element_present(driver, PASSWORD_INPUT) == True

    assert type_password(driver, "xzc456") == True

    assert attempt_login_enter_key(driver) == True

    WebDriverWait(driver, WAIT_TIME_DEFAULT_SEC).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//p[@class='error']"), "Please enter a username and password.")
    )
