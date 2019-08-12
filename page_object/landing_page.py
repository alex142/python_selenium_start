from page_object.base_object import BaseObject
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LandingPage(BaseObject):
    def __init__(self, driver):
        self.driver = driver
        self.input_form = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#navbar-brand-centered li.dropdown a")))
        #self.input_form = self.driver.find_element(By.CSS_SELECTOR, "div#navbar-brand-centered li.dropdown a")

    def click_landing_page(self):
        self.input_form.click()
        sleep(5)
