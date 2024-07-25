from locators.restore_password_page_locators import RestorePasswordPageLocators

class RestorePasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        email_input = self.driver.find_element(*RestorePasswordPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def click_restore_button(self):
        restore_button = self.driver.find_element(*RestorePasswordPageLocators.RESTORE_BUTTON)
        restore_button.click()

    def toggle_password_visibility(self):
        show_password_button = self.driver.find_element(*RestorePasswordPageLocators.SHOW_PASSWORD_BUTTON)
        show_password_button.click()
