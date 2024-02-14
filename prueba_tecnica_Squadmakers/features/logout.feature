
Feature: Logout app

Background:
Given I am on the login page https://www.saucedemo.com/
When I enter my username "standard_user" and my password "secret_sauce"
And I click on the login button
Then I should successfully log in

Scenario: Logout
When I click on the left dropdown menu
Then I click on logout
Then verify that it redirects  to the login paige