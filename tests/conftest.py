import pytest
import sys,os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",help="browser selecting here"
    )

    parser.addoption(
    "--headless",action="store_true",help="Run  browser in headless mode"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    headless= request.config.getoption("--headless")
    service_obj = Service()
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        if headless:
            chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=service_obj,options=chrome_options)
    elif browser_name =="edge":
        driver = webdriver.Edge(service=service_obj)
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported in my local machine")
    driver.implicitly_wait(5)
    logger.info(f"Launching {browser_name} browser(Headless={headless})")

    yield driver
    driver.quit()
    logger.info(f"Closed {browser_name} browserr")
