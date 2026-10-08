from guara.transaction import AbstractTransaction

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.login_page import LoginPage


class LoginTransaction(AbstractTransaction):

    def do(self, url, user, password):
        # navigate explicitly to the page
        self._driver.get(url)

        page = LoginPage(self._driver)
        page.login(user, password)

        # wait until inventory page loads (login success)
        WebDriverWait(self._driver, 15).until(
            lambda driver: "inventory" in driver.current_url.lower()
        )

        return self._driver.current_url
