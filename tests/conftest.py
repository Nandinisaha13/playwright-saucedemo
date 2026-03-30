import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD

@pytest.fixture(scope="function")
def page():
    # print("Launching browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page= browser.new_page()
        yield page
        # print("Closing browser")
        browser.close()
@pytest.fixture
def logged_in_page(page):
    login_page= LoginPage(page)
    login_page.navigate(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)