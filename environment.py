from browser import Browser
from pages.forgot_password_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage

def before_all(context):  # se initializeaza toate aceste obiecte inainte de fiecare test in parte
    context.browser = Browser()  # e vorba de clasa noastra creata deja - este un obiect al clasei browser
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.home_page = HomePage()
    context.base_page = BasePage()


def after_all(context):
    context.browser.close() # este apelata metoda close din clasa Browser - metoda def close din clasa Browser



