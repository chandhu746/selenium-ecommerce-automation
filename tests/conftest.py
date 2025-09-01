import pytest,json
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

    parser.addoption(
        "--site", action="store", default="rahulshetty", help="Which website config to use (rahulshetty/saucedemo)"
    )
# Loading config based on my input
def load_config(config_name):
    with open(f"config/{config_name}.json") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    headless= request.config.getoption("--headless")
    site = request.config.getoption("site")

    config = load_config(site)

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
    driver.get(config["base_url"])
    logger.info(f"Launching {browser_name} browser(Headless={headless}) on {site} website")

    yield driver,config
    driver.quit()
    logger.info(f"Closed {browser_name} browserr")
