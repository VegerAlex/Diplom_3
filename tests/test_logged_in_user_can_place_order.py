import pytest
from page_objects.main_page import MainPage
from page_objects.login_page import LoginPage
from page_objects.constructor_page import ConstructorPage


@pytest.mark.usefixtures("driver")
class TestOrder:
    def test_logged_in_user_can_place_order(self):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        constructor_page = ConstructorPage(self.driver)

        main_page.go_to_login_page()
        login_page.login("user@example.com", "password")
        main_page.go_to_constructor()

        constructor_page.add_ingredient("ingredient_id")
        constructor_page.place_order()

        assert "order-confirmation" in self.driver.current_url
