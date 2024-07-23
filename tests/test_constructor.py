import pytest
from page_objects.main_page import MainPage
from page_objects.constructor_page import ConstructorPage

@pytest.mark.usefixtures("driver")
class TestConstructor:
    def test_go_to_constructor(self):
        main_page = MainPage(self.driver)
        main_page.go_to_constructor()
        assert "constructor" in self.driver.current_url

    def test_ingredient_details_modal(self):
        main_page = MainPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        main_page.go_to_constructor()
        constructor_page.add_ingredient_to_order()
        modal = self.driver.find_element(*ConstructorPageLocators.MODAL_WINDOW)
        assert modal.is_displayed()
        constructor_page.close_modal()
        assert not modal.is_displayed()
