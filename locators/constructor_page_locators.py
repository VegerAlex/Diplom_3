from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    INGREDIENT_ITEM = (By.CLASS_NAME, "ingredient-item")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    MODAL_WINDOW = (By.CLASS_NAME, "modal")
    CLOSE_MODAL_BUTTON = (By.CLASS_NAME, "modal__close")

