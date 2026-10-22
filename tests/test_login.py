import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.excel_reader import read_excel


test_data = read_excel()


@pytest.mark.parametrize(
    "username,password",
    test_data
)
def test_login(browser_page, username, password):

    page = browser_page

    page.goto(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(page)

    login.login(
        username,
        password
    )

    inventory = InventoryPage(page)

    assert inventory.get_title() == "Products"
