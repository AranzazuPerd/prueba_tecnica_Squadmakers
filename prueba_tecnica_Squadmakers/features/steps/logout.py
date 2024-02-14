import time

from behave import when, then

from selenium.webdriver.common.by import By


@when('I click on the left dropdown menu')
def step_click_dropdown(context):
    login_button = context.driver.find_element(By.CLASS_NAME, "bm-burger-button")
    login_button.click()
    time.sleep(1)


@then('I click on logout')
def step_click_logout(context):
    login_button = context.driver.find_element(By.ID, "logout_sidebar_link")
    login_button.click()


@then('verify that it redirects  to the login paige')
def step_check_init_page(context):
    time.sleep(1)
    expected_url = "https://www.saucedemo.com/"
    current_url = context.driver.current_url
    assert current_url == expected_url, f"The current URL is {current_url}, but expected {expected_url}"
