import pytest
from test_cases.base_test import BaseTest
from page_object.landing_page import LandingPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestExampleOne(BaseTest):

    def test_title(self):
        assert "Selenium Easy" in self.driver.title

    def test_button(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_landing_page()
