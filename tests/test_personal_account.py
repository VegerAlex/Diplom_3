import pytest
from page_objects.main_page import MainPage
from page_objects.personal_account_page import PersonalAccountPage

@pytest.mark.usefixtures("driver")
class TestPersonalAccount:
    def test_go_to_personal_account(self):
        main_page = MainPage(self.driver)
        main_page.go_to_personal_account()
        assert "account" in self.driver.current_url

    def test_go_to_order_history(self):
        main_page = MainPage(self.driver)
        personal_account_page = PersonalAccountPage(self.driver)
        main_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        assert "orders" in self.driver.current_url

    def test_logout(self):
        main_page = MainPage(self.driver)
        personal_account_page = PersonalAccountPage(self.driver)
        main_page.go_to_personal_account()
        personal_account_page.logout()
        assert "login" in self.driver.current_url
