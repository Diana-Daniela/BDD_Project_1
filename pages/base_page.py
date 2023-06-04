from time import sleep

from selenium.webdriver.common.by import By

from browser import Browser


# in aceasta pagina punem toate metodele care sunt utile in orice pagina
# si nu neparat specifice doar unei pagini
class BasePage(Browser):
    LOGIN_BUTTON = (By.CLASS_NAME, "ico-login")
    MY_ACCOUNT = (By.CLASS_NAME, "ico-account")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def verify_my_account_is_displayed(self):
        sleep(1)
        assert self.driver.find_element(*self.MY_ACCOUNT).is_displayed(), f"My Account is not displayed in the menu"

    def check_the_current_url(self, url):
        actual = self.driver.current_url
        assert actual == url, f"Url-ul este gresit"

