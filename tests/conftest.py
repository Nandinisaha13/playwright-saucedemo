import pytest
from playwright.sync_api import sync_playwright
import pytest_html

@pytest.fixture(scope="function")
def page():
    # print("Launching browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page= browser.new_page()
        yield page
        # print("Closing browser")
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)