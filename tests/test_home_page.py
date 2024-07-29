import allure
import selenium
import pytest
from data import Answers
import urls
from pages.home_page import HomePage


class TestHomePage:

    @pytest.mark.parametrize(
        "question_num, expected_result",
        [
            (0, Answers.ANSWER_1),
            (1, Answers.ANSWER_2),
            (2, Answers.ANSWER_3),
            (3, Answers.ANSWER_4),
            (4, Answers.ANSWER_5),
            (5, Answers.ANSWER_6),
            (6, Answers.ANSWER_7),
            (7, Answers.ANSWER_8)

        ]
    )
    @allure.title("Проверка списка в разделе 'Вопросы о важном' на главной странице")
    def test_question_and_answer(self, question_num, expected_result):
        home_page = HomePage(driver)
        home_page.get_url(urls.HOME_PAGE_URL)
        result = home_page.click_on_question_and_get_answer_text(
            question_num
        )

        assert result == expected_result

