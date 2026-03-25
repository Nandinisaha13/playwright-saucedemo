import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected",[
 ("standard_user", "secret_sauce", "success"), 
 ("invalid_user", "wrong_password", "failure"),
 ("locked_out_user", "secret_sauce", "locked")])
def test_login(page,username, password, expected):
   
    login_page= LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(username, password)

    if expected == "success":
            assert "inventory" in page.url
    elif expected== "failure":
            assert "do not match" in login_page.get_error_message().lower()
    elif expected== "locked":
            assert "locked out" in login_page.get_error_message().lower()
