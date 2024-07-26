import allure
import selenium
import pytest
from data import OrdersButtons
import helpers
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @pytest.mark.parametrize(
"OrdersButtons.BUTTON_ORDER_HEAD", "OrdersButtons.BUTTON_ORDER_DOWN"
    )


    @allure.description("Проверка оформления самоката")
    def order_scooter(self):

        order_page = OrderPage(driver)
        @allure.step(f"Переходим на домашнюю странцу{helpers.HOME_PAGE_URL}")
        order_page.get(helpers.ORDER_PAGE_URL)
        @allure.step("Кликаем на кнопку 'Заказать'")
        order_page.click_on_order_button()
        @allure.step("Заполняем поле 'Имя'")
        order_page.set_text_input_name()
        @allure.step("Заполняем поле 'Фамилия'")
        order_page.set_text_input_surname()
        @allure.step("Заполняем поле 'Адрес'")
        order_page.set_text_input_address()
        @allure.step("Раскрываем список станций метро")
        order_page.click_on_element_underground_list()
        @allure.step("Выбираем станцию метро")
        order_page.click_on_element_underground_station()
        @allure.step("Заполняем поле 'Телефон'")
        order_page.set_text_input_telephone()
        @allure.step("Нажимаем 'Далее'")
        order_page.click_on_element_next()
        @allure.step("Открываем календарь")
        order_page.click_on_calendar()
        @allure.step("Выбираем дату доставки")
        order_page.select_date_of_delivery()
        @allure.step("Выбираем продолжительность аренды")
        order_page.click_on_period_of_rent()
        @allure.step("Выбираем цвет")
        order_page.select_colour()
        @allure.step("Кликаем 'Заказать'")
        order_page.click_on_order_button()
        @allure.step("Подтверждаем")
        order_page.click_agree_form()
        @allure.step("Проверяем в форме подтверждения наличие текста 'Заказ оформлен'")
        order_page.get_text_from_element(result)

        assert order_page.find_element(*OrderPageLocators.NUMBER_ORDER).text == "Заказ оформлен"

    @allure.description("Проверяем переход на домашнюю страницу")
    def move_to_home_page(self):

        order_page = OrderPage(driver)

        @allure.step("Кликаем на кнопку 'Заказать'")
        order_page.click_on_order_button()

        @allure.step("Кликаем на лого самоката")
        order_page.click_on_scooter_logo()

        assert order_page.find_element(*OrderPageLocators.HOME_PAGE_TITLE).text == "Самокат на пару дней"



