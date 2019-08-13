from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_selenium_start.helpers.logger import LOGGER


def find_element_explicitly(driver, element_locator):
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element_locator))
    return element


def click_on_element(driver, element_locator):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_locator))
    element.click()



def populate_text_field(element, text):
    element.clear()
    element.send_keys(text)


def get_dropdown_values(driver, dropdown_locator_css):
    click_on_element(driver, (By.CSS_SELECTOR, dropdown_locator_css))
    #LOGGER.info("trying to retrieve elements")
    elements = driver.find_elements(By.CSS_SELECTOR, str(dropdown_locator_css) + " ul li a")
    #LOGGER.info(elements[0].get_attribute('text'))
    element_values = [item.get_attribute('text') for item in elements]
    #LOGGER.info(element_values)
    return element_values


