from selenium import webdriver
# from functions.basic import Base
from functions.constants import Constant as cs

class Browser():
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_browser(self,URL=cs.URL):
        self.driver.get(URL)

