import pytest
from guara.application import Application

pytest_plugins = ["tests.fixtures.driver"]


@pytest.fixture
def app(driver):
    return Application(driver)
