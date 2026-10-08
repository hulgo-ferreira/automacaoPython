from selenium.webdriver.common.by import By
from guara.transaction import AbstractTransaction


class RemoveFromCartTransaction(AbstractTransaction):

    REMOVE_ITEM = (By.ID, "remove-sauce-labs-backpack")

    def do(self):
        self._driver.find_element(*self.REMOVE_ITEM).click()
        return self._driver.current_url
