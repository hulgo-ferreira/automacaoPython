import time
 
from tests.fixtures.driver import driver
from selenium.webdriver.common.by import By
 
 
# =========================================================
# CENÁRIO 1 - CHECKOUT SEM PREENCHER DADOS
# =========================================================
 
def test_checkout_sem_preencher_dados(driver):
 
    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
 
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
    # 2. ADICIONAR PRODUTO
    # =========================
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()
    time.sleep(2)
 
    # =========================
    # 3. ACESSAR CARRINHO
    # =========================
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()
    time.sleep(2)
 
    assert "cart.html" in driver.current_url
 
    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    driver.find_element(
        By.ID,
        "checkout"
    ).click()
    time.sleep(2)
 
    assert "checkout-step-one.html" in driver.current_url
 
    # =========================
    # 5. TENTAR CONTINUAR SEM PREENCHER DADOS
    # =========================
    driver.find_element(
        By.ID,
        "continue"
    ).click()
    time.sleep(2)
 
    # =========================
    # 6. VALIDAR MENSAGEM DE ERRO
    # =========================
    mensagem = driver.find_element(
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    )
 
    assert mensagem.is_displayed()
    assert "First Name is required" in mensagem.text
 
    time.sleep(2)
 
 
# =========================================================
# CENÁRIO 2 - CHECKOUT PARCIAL
# =========================================================
 
def test_checkout_parcial(driver):
 
    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")
    time.sleep(2)
 
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
    # 2. ADICIONAR PRODUTO
    # =========================
    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()
    time.sleep(2)
 
    # =========================
    # 3. ACESSAR CARRINHO
    # =========================
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()
    time.sleep(2)
 
    assert "cart.html" in driver.current_url
 
    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    driver.find_element(
        By.ID,
        "checkout"
    ).click()
    time.sleep(2)
 
    assert "checkout-step-one.html" in driver.current_url
 
    # =========================
    # 5. PREENCHER APENAS PARTE DOS DADOS
    # =========================
    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Alessandro")
    time.sleep(1)
 
    # Não preencher Last Name e Postal Code
 
    # =========================
    # 6. TENTAR CONTINUAR
    # =========================
    driver.find_element(
        By.ID,
        "continue"
    ).click()
    time.sleep(2)
 
    # =========================
    # 7. VALIDAR MENSAGEM DE ERRO
    # =========================
    mensagem = driver.find_element(
        By.CSS_SELECTOR,
        "h3[data-test='error']"
    )
 
    assert mensagem.is_displayed()
    assert "Last Name is required" in mensagem.text
 
    time.sleep(2)