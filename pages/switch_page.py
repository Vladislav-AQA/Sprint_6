import selenium
import urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage



class SwitchPage(BasePage):


    @allure.step("Перейти на домашнюю веб-страницу")
    def get_url(self):
        self.get(urls.HOME_PAGE_URL)


    @allure.step("Принять куки")
    def accept_cookies(self):
        el = self.find_element(*HomePageLocators.COOKIES_BUTTON)
        el.click()


    @allure.step("Кликнуть на лого сайта")
    def click_on_element(self, locator):
        el = self.find_element(*HomePageLocators.SAMOKAT_LOGO)
        el.click()


    @allure.step("Переключиться на новую вкладку")
    def switch_to_window(self):
        self.switch_to_window(self.window_handless[2])


    @allure.step("Получить текст всплывающего окна в новой вкладке")
    def get_text_from_element(self, locator):
        el = self.driver.find_element(*HomePageLocators.INSTALL_BUTTON_YANDEX_PAGE)
        return el.text("Установить")
