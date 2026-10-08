from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.login_page import LoginPage


def test_login_com_credenciais_invalidas(driver):
    driver.get("https://www.saucedemo.com")

    page = LoginPage(driver)
    page.login("invalid_user", "wrong_password")

    mensagem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert mensagem.is_displayed()
    assert "Username and password do not match" in mensagem.text or mensagem.text != ""
