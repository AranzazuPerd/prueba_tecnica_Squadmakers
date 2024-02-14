Feature: Buy one product

  Background:
    Given I am on the login page https://www.saucedemo.com/
    When I enter my username "standard_user" and my password "secret_sauce"
    And I click on the login button
    Then I should successfully log in

 Scenario Outline: Buy product
    When I select the item to buy
    And add to item on the cart
    And I click on the cart
    Then it takes us to the cart page
    Then verify that the product is <product>
    And verify that the price is <expected_price>
    And click on checkout
    Then it takes us to the checkout page
    And fill out the form with "<name>", "<lastname>", "<postal_code>"
    And click on continue
    Then verify that the total purchase is <total_price>
    And click on finish
    Then check that it displays the following message: <message>

    Examples:
      |product| expected_price | name  | lastname | postal_code | total_price | message |
      |Sauce Labs Backpack| 29.99           | John    | Doe      | 12345         | 32.39       | Thank you for your order! |
