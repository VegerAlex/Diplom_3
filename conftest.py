import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope="session", autouse=True)
def setup_allure_environment():
    allure.environment(browser="Chrome and Firefox", environment="Testing")

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.quit()
