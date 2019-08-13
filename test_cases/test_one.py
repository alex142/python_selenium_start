import pytest

from python_selenium_start.page_object.landing_page import LandingPage
from python_selenium_start.test_cases.base_test import BaseTest
from python_selenium_start.helpers.logger import LOGGER


class TestExampleOne(BaseTest):
    '''
    def test_title(self):
        assert "Selenium Easy" in self.driver.title

    def test_button(self):
        landing_page = LandingPage(self.driver)
        landing_page.click_landing_page()
        LOGGER.info("Test method 1")
    '''

    def test_options(self):
        landing_page = LandingPage(self.driver)
        options = landing_page.parse_table()
        LOGGER.info("Options = %s" % len(options))

