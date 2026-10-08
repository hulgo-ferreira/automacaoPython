from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.login_page import LoginPage

def _login_standard_user(driver):
    driver.get("https://www.saucedemo.com")
    page = LoginPage(driver)
    page.login("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url

def _get_product_prices(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price"))
    )

    elementos_preco = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    return [float(elemento.text.replace("$", "")) for elemento in elementos_preco]

def _get_product_names(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name"))
    )

    elementos_nome = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return [elemento.text for elemento in elementos_nome]

def _select_sort_option(driver, value):
    select_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']"))
    )
    Select(select_element).select_by_value(value)

def test_ordenar_produtos_por_preco_crescente(driver):
    _login_standard_user(driver)
    _select_sort_option(driver, "lohi")

    precos_tela = _get_product_prices(driver)
    precos_esperados = sorted(precos_tela)

    assert precos_tela == precos_esperados, (
        f"Ordem incorreta para preço crescente. Atual: {precos_tela} "
        f"Esperado: {precos_esperados}"
    )

def test_ordenar_produtos_de_a_para_z(driver):
    _login_standard_user(driver)
    _select_sort_option(driver, "az")

    nomes_tela = _get_product_names(driver)
    nomes_esperados = sorted(nomes_tela)

    assert nomes_tela == nomes_esperados, (
        f"Ordem incorreta de A-Z. Atual: {nomes_tela} "
        f"Esperado: {nomes_esperados}"
    )

def test_ordenar_produtos_de_z_para_a(driver):
    _login_standard_user(driver)
    _select_sort_option(driver, "za")

    nomes_tela = _get_product_names(driver)
    nomes_esperados = sorted(nomes_tela, reverse=True)

    assert nomes_tela == nomes_esperados, (
        f"Ordem incorreta de Z-A. Atual: {nomes_tela} "
        f"Esperado: {nomes_esperados}"
    )
