import pytest

from tests.data.data_loader import load_data


@pytest.fixture
def login_data():
    return load_data("login_data.json")
