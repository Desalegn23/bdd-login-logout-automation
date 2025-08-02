Feature: Login and Logout user flow
  As a user of saucedemo.com
  I want to login and logout successfully

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should see the dashboard

  Scenario: Logout from the dashboard
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I logout
    Then I should be redirected to the login page
