"""Setting instance for the browser."""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Fixture for creating a Chrome browser instance.
    Function attached to the testbefore the test is run.
    Setting the paramaters for the selenium test.
    """
    options = Options()
    # set the running of the browser in the background
    options.headless = False
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()
