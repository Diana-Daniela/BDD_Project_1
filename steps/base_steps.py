from behave import *

@when('base: I click on login button')
def step_impl(context):
    context.base_page.click_login_button()

@then('base: Ckeck the url to be "{url}"')
def step_impl(context,url):
    context.base_page.check_the_current_url(url)

