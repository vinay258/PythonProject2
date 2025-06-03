import pytest
from selenium import webdriver
from config.credentials import*


@pytest.fixture(scope="function")
def vinay():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    print("iam opening facebook url")
    yield driver
    print("iam quiting the url")
    driver.quit()

@pytest.fixture(scope="module")
def vinaykumar():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(demo_site_url)
    print("iam opening facebook url")
    yield driver
    print("iam quiting the url")
    driver.quit()


@pytest.fixture(scope="function")
def form_filling():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(demo_site_url)
    print("iam opening demo site url")
    yield driver
    print("iam quiting the url")
    driver.quit()


@pytest.fixture(scope="function")
def web_table():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(web_table_url)
    print("iam opening demo site url")
    yield driver
    print("iam quiting the url")
    driver.quit()


@pytest.fixture(scope="function")
def web_table1():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(herouk_table_url)
    print("iam opening demo site url")
    yield driver
    print("iam quiting the url")
    driver.quit()






