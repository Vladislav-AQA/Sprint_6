from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:


    def __init__(self, driver):
        self.driver = driver


    @allure.step("Перейти на веб-страницу")
    def get_url(self, URL):
        self.driver.get(URL)


    @allure.step("Найти элемент с ожиданием")
    def find_element(self, locator):
        WebDriverWait(
            self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator):
        el = self.find_element(locator)
        el.click()


    @allure.step("Получить текст элемента")
    def get_text_from_element(self, locator):
        el = self.find_element(locator)
        return el.text()


    @allure.step("Ввести текст")
    def set_text_input(self, locator, text):
        el = self.find_element(locator)
        el.send_keys(text)


    @allure.step("Форматировать локаторы раздела 'Вопрос-ответ'")
    def format_locator(self, locator, num):
        method, locator = locator
        locator = locator.format(num)
        return (method, locator)

    @allure.step("Переключить на новую вкладку")
    def switch_to_window(self, num):
        self.driver.switch_to_window(self.window_handless[num])
