from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver


from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.continue_shopping_transaction import (
    ContinueShoppingTransaction,
)


def test_continue_shopping_a_partir_do_carrinho(app):
    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce"
    ).then(
        it.Contains,
        "inventory"
    )

    app.when(
        AddToCartTransaction
    ).asserts(
        it.Contains,
        "cart"
    )

    app.when(
        ContinueShoppingTransaction
    ).asserts(
        it.Contains,
        "inventory"
    )
