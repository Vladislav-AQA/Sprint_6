import allure
import selenium
import pytest
from data import OrdersButtons
import urls
from pages.order_page import OrderPage


class TestOrderPage:


    @pytest.mark.parametrize(
"OrdersButtons.BUTTON_ORDER_HEAD", "OrdersButtons.BUTTON_ORDER_DOWN"
    )


    @allure.title("Проверка оформления самоката")
    def test_order_scooter(self):

        order_page = OrderPage(driver)
        order_page.get(urls.ORDER_PAGE_URL)
        order_page.click_on_order_button()
        order_page.set_text_input_name()
        order_page.set_text_input_surname()
        order_page.set_text_input_address()
        order_page.click_on_element_underground_list()
        order_page.click_on_element_underground_station()
        order_page.set_text_input_telephone()
        order_page.click_on_element_next()
        order_page.click_on_calendar()
        order_page.select_date_of_delivery()
        order_page.click_on_period_of_rent()
        order_page.select_colour()
        order_page.click_on_order_button()
        order_page.click_agree_form()
        order_page.get_text_from_order_form

        assert order_page.get_text_from_order_form == "Заказ оформлен"

    @allure.title("Проверка перехода на домашнюю страницу")
    def test_move_to_home_page(self):

        order_page = OrderPage(driver)
        order_page.click_on_order_button()
        order_page.click_on_scooter_logo()

        assert order_page.get_text_from_home_page == "Самокат на пару дней"



