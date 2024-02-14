
Feature: Logout app

Background:
Given the login page
When enter my username and password
And I click on the login button
Then I should successfully log in

Scenario: Logout
When I click on the left dropdown menu
Then I click on logout
Then verify that it redirects  to the login paige