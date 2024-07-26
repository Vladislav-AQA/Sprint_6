import allure
import selenium
import pytest
from data import OrdersButtons
import helpers
from pages.switch_page import SwitchPage
from locators.home_page_locators import HomePageLocators

class TestSwitchPage:

    switch_page = SwitchPage(driver)
    @allure.step(f"Переходим на домашнюю странцу{helpers.HOME_PAGE_URL}")
    switch_page.get_url(helpers.HOME_PAGE_URL)

    @allure.step("Кликаем по надписи 'Яндекс'")
    switch_page.click_on_element()

    @allure.step("Переключаемся на вкладку Яндекса")
    switch_page.switch_to_window()

    @allure.step("Проверяем наличие 'dzen.ru' в адресе новой страницы")
    assert "dzen.ru" in helpers.DZEN_PAGE

