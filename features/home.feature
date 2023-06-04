Feature: Check the home page functionality

  Background:
    Given home: I am on home page

  @Test333
  Scenario: Click on login button and check the url
    When base: I click on login button
    Then base: Ckeck the url to be "https://demo.nopcommerce.com/login?returnUrl=%2F"

