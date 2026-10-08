import time
 
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By
 
 
# =========================================================
# CENÁRIO - RESETAR CARRINHO
# =========================================================
 
def test_resetar_carrinho(driver):
 
    # =========================
    # 1. ACESSAR PÁGINA DE LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
 
    # =========================
    # 2. REALIZAR LOGIN
    # =========================
    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")
    time.sleep(1)
 
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")
    time.sleep(1)
 
    driver.find_element(
        By.ID,
        "login-button"
    ).click()
    time.sleep(2)
 
    # =========================
    # 3. ADICIONAR PRODUTO AO CARRINHO
    # =========================
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()
    time.sleep(2)
 
    # =========================
    # 4. VALIDAR QUE O CARRINHO POSSUI ITEM
    # =========================
    carrinho = driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )
 
    assert carrinho.is_displayed()
    assert carrinho.text == "1"
 
    time.sleep(2)
 
    # =========================
    # 5. ABRIR MENU
    # =========================
    driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    ).click()
    time.sleep(2)
 
    # =========================
    # 6. RESETAR ESTADO DA APLICAÇÃO
    # =========================
    driver.find_element(
        By.ID,
        "reset_sidebar_link"
    ).click()
    time.sleep(3)
 
    # =========================
    # 7. VALIDAR QUE O CARRINHO ESTÁ VAZIO
    # =========================
    badges = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )
 
    assert len(badges) == 0
 
    time.sleep(2)