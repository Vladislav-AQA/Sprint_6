import selenium
import helpers
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):

    def get_url(self, URL):
        self.get_url(helpers.HOME_PAGE_URL)

    def accept_cookies(self):
        el = self.find_element(*HomePageLocators.COOKIES_BUTTON)
        el.click()

    def click_on_question_and_get_answer_text(self, num):
        formatted_question_locator = self.format_locator(HomePageLocators.QUESTION, num)
        formatted_answer_locator = self.format_locator(HomePageLocators.ANSWER, num)
        self.click_on_element(formatted_question_locator)
        return self.get_text_from_element(formatted_answer_locator)


