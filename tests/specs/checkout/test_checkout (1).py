import time
 
from tests.fixtures.driver import driver

from selenium.webdriver.common.by import By
 
 
# =========================================================

# CENÁRIO 1 - ORDENAR PRODUTOS POR PREÇO CRESCENTE

# =========================================================
 
def test_ordenar_produtos_por_preco_crescente(driver):
 
    # =========================

    # 1. LOGIN

    # =========================

    driver.get("https://www.saucedemo.com")

    time.sleep(1)
 
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    time.sleep(1)
 
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    time.sleep(1)
 
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
 
    # =========================

    # 2. SELECIONAR ORDENAÇÃO

    # =========================

    ordenacao = driver.find_element(

        By.CLASS_NAME,

        "product_sort_container"

    )
 
    ordenacao.click()

    time.sleep(1)
 
    driver.find_element(

        By.CSS_SELECTOR,

        "option[value='lohi']"

    ).click()

    time.sleep(1)
 
    # =========================

    # 3. OBTER PREÇOS

    # =========================

    produtos = driver.find_elements(

        By.CLASS_NAME,

        "inventory_item_price"

    )
 
    precos = []
 
    for produto in produtos:

        preco = float(

            produto.text.replace("$", "")

        )

        precos.append(preco)
 
    # =========================

    # 4. VALIDAR ORDENAÇÃO

    # =========================

    assert precos == sorted(precos)
 
 
# =========================================================

# CENÁRIO 2 - ORDENAR PRODUTOS POR NOME

# =========================================================
 
def test_ordenar_produtos_por_nome(driver):
 
    # =========================

    # 1. LOGIN

    # =========================

    driver.get("https://www.saucedemo.com")

    time.sleep(1)
 
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    time.sleep(1)
 
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    time.sleep(1)
 
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
 
    # =========================

    # 2. SELECIONAR ORDENAÇÃO

    # =========================

    ordenacao = driver.find_element(

        By.CLASS_NAME,

        "product_sort_container"

    )
 
    ordenacao.click()

    time.sleep(1)
 
    driver.find_element(

        By.CSS_SELECTOR,

        "option[value='az']"

    ).click()

    time.sleep(1)
 
    # =========================

    # 3. OBTER NOMES DOS PRODUTOS

    # =========================

    produtos = driver.find_elements(

        By.CLASS_NAME,

        "inventory_item_name"

    )
 
    nomes = [produto.text for produto in produtos]
 
    # =========================

    # 4. VALIDAR ORDENAÇÃO

    # =========================

    assert nomes == sorted(nomes)