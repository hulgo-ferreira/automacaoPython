from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver
from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction

def test_adicionar_item_ao_carrinho(app):
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
        it.IsEqualTo,
        "1"
    )


from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.remove_from_cart_transaction import (
    RemoveFromCartTransaction,
)


def test_remover_item_do_carrinho(app):
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
        it.IsEqualTo,
        "1"
    )

    app.when(
        RemoveFromCartTransaction
    ).asserts(
        it.IsEqualTo,
        "0"
    )
