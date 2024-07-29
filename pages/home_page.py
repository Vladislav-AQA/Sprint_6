import selenium
import urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure



class HomePage(BasePage):

    @allure.step("Перейти на домашнюю веб-страницу")
    def get_url(self):
        self.driver.get(urls.HOME_PAGE_URL)


    @allure.step("Принять куки")
    def accept_cookies(self):
        el = self.find_element(*HomePageLocators.COOKIES_BUTTON)
        el.click()


    @allure.step("Проверить соответствие вкладок вопрос-ответ")
    def click_on_question_and_get_answer_text(self, num):
        formatted_question_locator = self.format_locator(HomePageLocators.QUESTION, num)
        formatted_answer_locator = self.format_locator(HomePageLocators.ANSWER, num)
        self.click_on_element(formatted_question_locator)
        return self.get_text_from_element(formatted_answer_locator)


