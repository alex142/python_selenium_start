import sys
import os

sys.path.insert(0, os.path.abspath("."))

import pytest
from selenium import webdriver
from data import settings



@pytest.fixture(scope="class")
def driver_init(request):
    print("initiating web driver")
    driver = webdriver.Chrome()
    driver.get(settings.base_url)
    driver.maximize_window()
    request.cls.driver = driver

    def teardown():
        print("closing the driver")
        driver.close()

    request.addfinalizer(teardown)

    return driver

