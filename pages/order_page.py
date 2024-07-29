import selenium
import urls
import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):


    @allure.step("Перейти на домашнюю веб-страницу")
    def get_url(self):
        self.get(urls.HOME_PAGE_URL)

    @allure.step("Принять куки")
    def accept_cookies(self):
        el = self.find_element(*OrderPageLocators.COOKIES_BUTTON)
        el.click()


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        el = self.find_element(*OrderPageLocators.ORDER_BUTTON_HEAD)
        el.click()


    @allure.step("Ввести текст в поле 'Имя'")
    def set_text_input_name(self, locator, text):
        el = self.find_element(*OrderPageLocators.NAME_INPUT)
        el.send_keys("Иван")


    @allure.step("Ввести текст в поле 'Фамилия'")
    def set_text_input_surname(self, locator, text):
        el = self.find_element(*OrderPageLocators.SURNAME_INPUT)
        el.send_keys("Иванов")


    @allure.step("Ввести текст в поле 'Адрес'")
    def set_text_input_address(self, locator, text):
        el = self.find_element(*OrderPageLocators.ADDRESS_INPUT)
        el.send_keys("Москва")


    @allure.step("Кликнуть по списку метро")
    def click_on_element_underground_list(self, locator):
        el = self.find_element(*OrderPageLocators.UNDERGROUND_INPUT)
        el.click


    @allure.step("Выбрать станцию метро")
    def click_on_element_underground_station(self, locator):
        el = self.find_element(*OrderPageLocators.UNDERGROUND_STATION)
        el.click()


    @allure.step("Ввести текст в поле 'Телефон'")
    def set_text_input_telephone(self, locator, text):
        el = self.find_element(*OrderPageLocators.TELEPHONE_NUMBER_INPUT)
        el.send_keys("88003553535")


    @allure.step("Кликнуть 'Далее'")
    def click_on_element_next(self, locator):
        el = self.find_element(*OrderPageLocators.NEXT_BUTTON)
        el.click()


    @allure.step("Кликнуть на календарь")
    def click_on_calendar(self, locator):
        el = self.find_element(*OrderPageLocators.CALENDAR)
        el.click()


    @allure.step("Выбрать дату доставки")
    def select_date_of_delivery(self, locator):
        el = self.find_element(*OrderPageLocators.DATE_SELECT)
        el.click()


    @allure.step("Выбрать период аренды")
    def click_on_period_of_rent(self):
        el = self.find_element(*OrderPageLocators.RENT_PERIOD)
        el.click()


    @allure.step("Выбрать цвет")
    def select_colour(self):
        el = self.find_element(*OrderPageLocators.CHECK_BOX_BLACK)
        el.click()


    @allure.step("Кликнуть 'Заказать'")
    def click_on_order_button(self):
        el = self.find_element(*OrderPageLocators.ORDER_BUTTON_RENT_FORM)
        el.click()


    @allure.step("Кликнуть на форму соглашения")
    def click_agree_form(self):
        el = self.find_element(*OrderPageLocators.AGREE_RENT_CONDITIONS)
        el.click()


    @allure.step("Получить текст формы успешного оформления заказа")
    def get_text_from_order_form(self, locator):
        el = self.find_element(*OrderPageLocators.NUMBER_ORDER)
        return el.text("Заказ оформлен")


    @allure.step("Кликнуть по лого сайта")
    def click_on_scooter_logo(self, locator):
        el = self.find_element(*OrderPageLocators.SAMOKAT_LOGO)
        el.click()

    @allure.step("Получить текст с домашней веб-страницы")
    def get_text_from_home_page(self, locator):
        el = self.find_element(*OrderPageLocators.HOME_PAGE_TITLE)
        return el.tex("Самокат на пару дней")
