import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from prueba_tecnica_Squadmakers.configurations.config import TestData


@given('the login page')
def step_init_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get(TestData.URL)


@when('enter my username and password')
def step_enter_user_password(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")
    user = TestData.USERNAME
    password = TestData.PASSWORD
    username_input.clear()
    username_input.send_keys(user)
    password_input.clear()
    password_input.send_keys(password)


@when('I click on the login button')
def step_click_login_button(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(3)


@then('I should successfully log in')
def step_success_login(context):
    time.sleep(2)
    expected_url = "https://www.saucedemo.com/inventory.html"
    current_url = context.driver.current_url
    assert current_url == expected_url, f"The current URL  is {current_url}, but expected {expected_url}"





