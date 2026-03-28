import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    # print("Launching browser")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page= browser.new_page()
        yield page
        # print("Closing browser")
        browser.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")