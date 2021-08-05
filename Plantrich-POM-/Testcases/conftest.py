from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver = webdriver.Chrome(executable_path="Resourses/chromedriver")
        driver.implicitly_wait(60)
        driver.maximize_window()
        print("Launching Chromebrowser")


    elif browser=='Firefox':
        driver = webdriver.Firefox(executable_path="Resourses/geckodriver")
        driver.implicitly_wait(60)
        driver.set_window_position(0, 1)
        print("Launching Firefoxbrowser")
    return driver

def pytest_addoption(parser):   #This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption("--browser")

