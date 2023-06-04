Feature: Check the Login functionality

  Background:
    Given login: I am a user on the login page
    When login: I click on the forgot password link - ???

  @login_test
  Scenario: Enter wrong credentials and check the error
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: It shown an error message "Login was unsuccessful."
