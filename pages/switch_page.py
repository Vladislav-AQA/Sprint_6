import selenium
import helpers
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SwitchPage(BasePage):


    def get_url(self, URL):
        self.get_url(helpers.HOME_PAGE_URL)

    def accept_cookies(self):
        el = self.find_element(*HomePageLocators.COOKIES_BUTTON)
        el.click()

    def click_on_element(self, locator):
        el = self.driver.find_element(*HomePageLocators.SAMOKAT_LOGO)
        el.click()

    def switch_to_window(self):
        self.driver.switch_to_window(driver.window_handless[2])

    def get_text_from_element(self, locator):
        el = self.driver.find_element(*HomePageLocators.INSTALL_BUTTON_YANDEX_PAGE)
        return el.text("Установить")
