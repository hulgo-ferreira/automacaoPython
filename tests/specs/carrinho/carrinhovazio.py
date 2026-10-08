import time
 
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By
 
 
# =========================================================
# CENÁRIO - ACESSAR CARRINHO SEM ITENS
# =========================================================
 
def test_acessar_carrinho_sem_itens(driver):
 
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
    # 3. ACESSAR O CARRINHO
    # =========================
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()
    time.sleep(3)
 
    # =========================
    # 4. VALIDAR PÁGINA DO CARRINHO
    # =========================
    assert "cart.html" in driver.current_url
 
    # =========================
    # 5. VALIDAR QUE O CARRINHO ESTÁ VAZIO
    # =========================
    produtos = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )
 
    assert len(produtos) == 0
 
    time.sleep(2)