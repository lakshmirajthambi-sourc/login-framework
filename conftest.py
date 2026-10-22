import pytest


import pytest

@pytest.fixture
def browser_page(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        channel="chrome"  # Uses system Chrome (or remove if using downloaded Playwright browser)
    )
    context = browser.new_context()
    page = context.new_page()
    
    yield page  # <-- Returning the page object to the test function
    
    context.close()
    browser.close()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("browser_page")

        if page:

            screenshot_name = (
                "screenshots/"
                + item.name
                + ".png"
            )

            page.screenshot(
                path=screenshot_name
            )
