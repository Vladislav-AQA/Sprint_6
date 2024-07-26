from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, URL):
        self.driver.get(URL)

    def find_element(self, locator):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.visibility_of_element_located(*locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.element_to_be_clickable(*locator))
        el = self.driver.find_element(*locator)
        el.click()

    def get_text_from_element(self, locator):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.visibility_of_element_located(*locator))
        el = self.driver.find_element(*locator)
        return el.text()

    def set_text_input(self, locator, text):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.visibility_of_element_located(*locator))
        el = self.driver.find_element(*locator)
        el.send_keys(text)

    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)