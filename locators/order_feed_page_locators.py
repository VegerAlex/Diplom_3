from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_ITEM = (By.CLASS_NAME, "order-item")
    COMPLETED_COUNT = (By.CLASS_NAME, "completed-count")
    TODAY_COMPLETED_COUNT = (By.CLASS_NAME, "today-completed-count")
    IN_PROGRESS_ORDERS = (By.CLASS_NAME, "in-progress-order")

