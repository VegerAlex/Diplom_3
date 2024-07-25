from selenium.webdriver.common.by import By

class RestorePasswordPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//button[@type='button']")
    PASSWORD_INPUT = (By.NAME, "password")

