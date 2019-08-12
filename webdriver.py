from selenium import webdriver

class Driver:

    def __init__(self):
        self.instance = webdriver.Chrome()