from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")

