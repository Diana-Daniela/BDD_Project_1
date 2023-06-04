  # trebuie sa aiba cuvantul "steps" la final in numele fisierului

from behave import *

@when ('forgot pass: I fill in my email "{email}"') # email va fi un parametru care va lua valoarea pusa intre "" si este cel de jos
def step_impl(context, email): # trebuie neaprata sa aiba denumirea step_impl
    context.forgot_password_page.set_email(email)  # nu trebuie sa fie acelasi email ca in metoda din _page

@when ('forgot pass: I click on the recover button')
def step_impl(context):
    context.forgot_password_page.click_recover_button()

@then ('forgot pass: I verify the invalid email validation message "{msg}"') # msg e un parametru care lua valoarea de wrong email
def step_impl(context, msg):
    context.forgot_password_page.verify_email_error_message(msg)

@then('forgot_pass: I verify the notification "{notify_message}"')
def step_impl(context,notify_message):
    context.forgot_password_page.verify_notification_message(notify_message)

@when('forgot_pass: I make sure the email input is cleared')
def step_impl(context):
    context.forgot_password_page.clean_email_text_field()

