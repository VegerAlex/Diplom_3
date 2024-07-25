import pytest
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.constructor_page import ConstructorPage
from page_objects.order_feed_page import OrderFeedPage


@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    def test_completed_orders_today_increases(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)

        main_page.go_to_login_page()
        login_page.login("user@example.com", "password")

        initial_count = order_feed_page.get_completed_orders_today_count()

        main_page.go_to_constructor()
        constructor_page.add_ingredient("ingredient_id")
        constructor_page.place_order()

        new_count = order_feed_page.get_completed_orders_today_count()

        assert new_count == initial_count + 1
