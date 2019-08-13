from python_selenium_start.page_object.base_object import BaseObject
from time import sleep
from python_selenium_start.extensions.web_driver_extensions import *
from python_selenium_start.helpers.incidend_grid import *





class LandingPage(BaseObject):
    def __init__(self, driver):
        self.driver = driver
        self.incidents_on_page = self.driver.find_elements(By.CSS_SELECTOR, "table#incident_table tbody tr")

    def parse_table(self):
        rows = [row for row in self.incidents_on_page]
        incident_grid = IncidentGrid()
        for row in rows:
            row_number = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)")
            row_problem = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)")
            row_priority = row.find_element(By.CSS_SELECTOR, "td:nth-child(9)")
            row_state = row.find_element(By.CSS_SELECTOR, "td:nth-child(10)")
            row_assignment = row.find_element(By.CSS_SELECTOR, "td:nth-child(11)")
            incident = Incident(row_number, row_problem.get_attribute('text'), row_priority.get_attribute('text'),
                                row_state.get_attribute('text'), row_assignment.get_attribute('text'))
            incident_grid.add_incident(incident)
        return incident_grid

    def open_incident(self, incident_number):
        grid = self.parse_table()
        incident = list(filter(lambda x: x.number == incident_number, grid))
        incident[0].open_incident()

