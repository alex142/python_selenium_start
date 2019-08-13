import sys
import os

sys.path.insert(0, os.path.abspath("."))

import pytest
from selenium import webdriver
from python_selenium_start.data import settings


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(executable_path=os.path.abspath("") + "\\driver\\chromedriver.exe")
    driver.get(settings.base_url)
    driver.maximize_window()
    request.cls.driver = driver


    def teardown():
        driver.close()

    request.addfinalizer(teardown)

    return driver
