from python_selenium_start.page_object.base_object import BaseObject
from time import sleep
from python_selenium_start.extensions.web_driver_extensions import *
import logging


class IncidentPage(BaseObject):
    def __init__(self, driver):
        self.driver = driver
        self.input_form_css = "div#navbar-brand-centered li.dropdown:nth-child(1)"
        self.input_form = find_element_explicitly(driver, (By.CSS_SELECTOR, self.input_form_css))
        # self.input_form = self.driver.find_element(By.CSS_SELECTOR, "div#navbar-brand-centered li.dropdown a")
