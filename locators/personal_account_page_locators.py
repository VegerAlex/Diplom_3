from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/profile/orders']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")

