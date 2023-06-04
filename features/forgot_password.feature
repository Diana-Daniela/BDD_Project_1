  # fisierul din
    # titlul il punem in Feature:
Feature: Check the Forgot password functionality
  # ne gandim ca la un setup din UnitSetup care se executa inaintea fiecarui test in parte:
  Background:
    Given login: I am a user on the login page
      #sa punem intai pagina in care ne aflam-login
    When login: I click on the forgot password link
    # suntem deja pe pass recovery:

  @smoke
  Scenario: Check validation error message when email is invalid format
    # mai sus i-am dat un nume scenariului
    When forgot pass: I fill in my email "my_email@"
    # pe pagina pe care ma aflu - forgot pass -scriem exact textul pe care vreau sa il pun pe pagina- argum se scrie intre ghilimele
    # il vom folosi mai departe ca si variabila sau parametru??
    When forgot pass: I click on the recover button
    Then forgot pass: I verify the invalid email validation message "Wrong email"
    # scriem mesajul de validare exact cum e pe pagina intre ghilimele ca sus

    # apoi trebuie sa scriem in steps cod Python echivalent cu scenariu de mai sus, cu decoratorii
      # dar mai intai trebuie sa ne cream Context - este fiecare pagina in parte pe care o putem apela
    # in fisierul environment - 2 metode trebuie scrise..

  @test
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @multiple_value_email
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notification>"

  Examples:
    |email         |expected_error|expected_notification|
    |test          |Wrong email   |None                 |
    |test@         |Wrong email   |None                 |
    |test.com      |Wrong email   |None                 |
    |test@mail.com |None          |Email not found.     |





