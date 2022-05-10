"""Setting instance for the browser."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# https://pypi.org/project/webdriver-manager/
from webdriver_manager.chrome import ChromeDriverManager


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
    # set the browser to run in incognito mode
    options.add_argument("--incognito")
    # set the browser variable to the chrome browser
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield browser
    browser.close()
