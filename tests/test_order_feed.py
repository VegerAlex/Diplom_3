import pytest
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage

@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    def test_open_order_details(self):
        main_page = MainPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        main_page.go_to_order_feed()
        order_feed_page.open_order_details()
        modal = self.driver.find_element(*OrderFeedPageLocators.MODAL_WINDOW)
        assert modal.is_displayed()
