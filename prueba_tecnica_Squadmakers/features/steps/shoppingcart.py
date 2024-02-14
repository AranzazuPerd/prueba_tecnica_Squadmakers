import time

from behave import given, when, then
from selenium.webdriver.common.by import By


@when('I select the item to buy')
def step_selecct_item(context):
    item = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div')
    item.click()


@when('add to item on the cart')
def step_click_cart_icon(context):
    add_to_cart_button = context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()


@when('I click on the cart')
def step_voy_al_carrito(context):
    cart_icon = context.driver.find_element(By.CLASS_NAME, "shopping_cart_container")
    cart_icon.click()


@then('it takes us to the cart page')
def step_cart_page(context):
    time.sleep(1)
    expected_url = "https://www.saucedemo.com/cart.html"
    current_url = context.driver.current_url
    assert current_url == expected_url, f"The current URL  {current_url}, expected {expected_url}"


@then('verify that the product is {product}')
def step_verify_product(context, product):
    element_div = context.driver.find_element(By.CLASS_NAME, "inventory_item_name")
    texto_div = element_div.text
    assert texto_div == product, f"The current product is {texto_div},but expected {product}"


@then('verify that the price is {price}')
def step_verify_price(context, price):
    element_div = context.driver.find_element(By.CLASS_NAME, "inventory_item_price")
    element_div_price_text = element_div.text
    current_price = float(element_div_price_text[1:])
    price = float(price)
    assert current_price == price, f"The current_price of product is {current_price}, but expected {price}"


@then('click on checkout')
def step_click_checkout(context):
    cart_icon_checkout = context.driver.find_element(By.ID, "checkout")
    cart_icon_checkout.click()


@then('it takes us to the checkout page')
def step_checkout_page(context):
    time.sleep(1)
    expected_url = "https://www.saucedemo.com/checkout-step-one.html"
    current_url = context.driver.current_url
    assert current_url == expected_url, f"The current url is {current_url}, but expected {expected_url}"


@then('fill out the form with {name},{lastname},{zip}')
def step_fill_form(context, name, lastname, zip):
    time.sleep(1)
    name_input = context.driver.find_element(By.ID, "first-name")
    lastname_input = context.driver.find_element(By.ID, "last-name")
    zip_input = context.driver.find_element(By.ID, "postal-code")

    name_input.clear()
    name_input.send_keys(name)
    lastname_input.clear()
    lastname_input.send_keys(lastname)
    zip_input.clear()
    zip_input.send_keys(zip)


@then('click on continue')
def step_click_continue(context):
    form_button_continue = context.driver.find_element(By.ID, "continue")
    form_button_continue.click()


@then('verify that the total purchase is {price}')
def step_check_purchase_price(context, price):
    element_div = context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div[8]")
    element_div_price_text = element_div.text
    current_price = float(element_div_price_text[8:])
    price = float(price)
    assert current_price == price, f"The current price of purchase is {current_price}, but expected {price}"


@then('click on finish')
def step_click_finish(context):
    button_finish = context.driver.find_element(By.ID, "finish")
    button_finish.click()


@then('check that it displays the following message: {message}')
def step_check_message_finish(context, message):
    time.sleep(1)
    element_div = context.driver.find_element(By.CLASS_NAME, "complete-header")
    texto_div = element_div.text
    assert texto_div == message, f"The finish message is {texto_div}, but expected {message}"
