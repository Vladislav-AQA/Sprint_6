from selenium.webdriver.common.by import By


class HomePageLocators:

    COOKIES_BUTTON = By.ID, "rcc-confirm-button"
    QUESTION = By.ID, "accordion__heading-{}"
    ANSWER = By.ID, "accordion__heading-{}"
    ORDER_BUTTON_HEAD = By.CLASS_NAME, "Button_Button__ra12g"
    ORDER_BUTTON_DOWN = By.CLASS_NAME, "Button_Button__ra12g Button_UltraBig__UU3Lp"