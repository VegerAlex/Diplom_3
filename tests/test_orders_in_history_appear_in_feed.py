import pytest
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.personal_account_page import PersonalAccountPage
from page_objects.order_feed_page import OrderFeedPage


@pytest.mark.usefixtures("driver")
class TestOrderHistory:
    def test_orders_in_history_appear_in_feed(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        personal_account_page = PersonalAccountPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)

        main_page.go_to_login_page()
        login_page.login("user@example.com", "password")
        main_page.go_to_personal_account()

        orders = personal_account_page.get_order_history()
        main_page.go_to_order_feed()

        for order in orders:
            assert order_feed_page.is_order_in_feed(order)
