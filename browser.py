from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10)  # asteapta 10 sec pana se incarca pagina respectiva pana sa arunce o exceptie

    def close(self):
        self.driver.quit()
