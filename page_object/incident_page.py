from python_selenium_start.page_object.base_object import BaseObject
from time import sleep
from python_selenium_start.extensions.web_driver_extensions import *
import logging


class IncidentPage(BaseObject):
    def __init__(self, driver):
        self.driver = driver


