import selenium
import helpers
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage(BasePage):

    def get_url(self, URL):
        self.get_url(helpers.HOME_PAGE_URL)

    def accept_cookies(self):
        el = self.find_element(*OrderPageLocators.COOKIES_BUTTON)
        el.click()

    def click_on_element(self, locator):
        el = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_HEAD)
        el.click()

    def set_text_input_name(self, locator, text):
        el = self.driver.find_element(*OrderPageLocators.NAME_INPUT)
        el.send_keys("Иван")

    def set_text_input_surname(self, locator, text):
        el = self.driver.find_element(*OrderPageLocators.SURNAME_INPUT)
        el.send_keys("Иванов")

    def set_text_input_address(self, locator, text):
        el = self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT)
        el.send_keys("Москва")

    def click_on_element_underground_list(self, locator):
        el = self.driver.find_element(*OrderPageLocators.UNDERGROUND_INPUT)
        el.click

    def click_on_element_underground_station(self, locator):
        el = self.driver.find_element(*OrderPageLocators.UNDERGROUND_STATION)
        el.click()

    def set_text_input_telephone(self, locator, text):
        el = self.driver.find_element(*OrderPageLocators.TELEPHONE_NUMBER_INPUT)
        el.send_keys("88003553535")

    def click_on_element_next(self, locator):
        el = self.driver.find_element(*OrderPageLocators.NEXT_BUTTON)
        el.click()


    def click_on_calendar(self, locator):
        el = self.driver.find_element(*OrderPageLocators.CALENDAR)
        el.click()

    def select_date_of_delivery(self, locator):
        el = self.driver.find_element(*OrderPageLocators.DATE_SELECT)
        el.click()

    def click_on_period_of_rent(self):
        el = self.driver.find_element(*OrderPageLocators.RENT_PERIOD)
        el.click()

    def select_colour(self):
        el = self.driver.find_element(*OrderPageLocators.CHECK_BOX_BLACK)
        el.click()

    def click_on_order_button(self):
        el = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_RENT_FORM)
        el.click()

    def click_agree_form(self):
        el = self.driver.find_element(*OrderPageLocators.AGREE_RENT_CONDITIONS)
        el.click()

    def get_text_from_element(self, locator):
        el = self.driver.find_element(*OrderPageLocators.NUMBER_ORDER)
        return el.text("Заказ оформлен")

    def click_on_scooter_logo(self, locator):
        el = self.driver.find_element(*OrderPageLocators.SAMOKAT_LOGO)
        el.click()

