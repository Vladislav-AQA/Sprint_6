import allure
import selenium
import pytest
import urls
from pages.switch_page import SwitchPage

class TestSwitchPage:

    @allure.title("Проверка перехода на новую вкладку")
    def test_switch_page(self):

         switch_page = SwitchPage(driver)
         switch_page.get_url(urls.HOME_PAGE_URL)
         switch_page.click_on_element()
         switch_page.switch_to_window()

    assert "dzen.ru" in urls.DZEN_PAGE

