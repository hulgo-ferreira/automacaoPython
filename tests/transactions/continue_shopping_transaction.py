from selenium.webdriver.common.by import By
from guara.transaction import AbstractTransaction


class ContinueShoppingTransaction(AbstractTransaction):

    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def do(self):
        self._driver.find_element(*self.CONTINUE_SHOPPING).click()
        return self._driver.current_url
