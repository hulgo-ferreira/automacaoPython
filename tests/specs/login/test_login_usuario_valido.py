from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.login_page import LoginPage

def test_login_com_usuario_valido(driver):
    driver.get("https://www.saucedemo.com")
    page = LoginPage(driver)
    page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    assert "inventory" in driver.current_url