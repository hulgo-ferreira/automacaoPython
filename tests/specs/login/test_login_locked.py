from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.login_page import LoginPage


def test_login_usuario_bloqueado(driver):
    driver.get("https://www.saucedemo.com")

    page = LoginPage(driver)
    page.login("locked_out_user", "secret_sauce")

    mensagem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert mensagem.is_displayed()
    assert "locked out" in mensagem.text.lower()
