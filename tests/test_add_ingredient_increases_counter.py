import pytest
from page_objects.main_page import MainPage
from page_objects.constructor_page import ConstructorPage


@pytest.mark.usefixtures("driver")
class TestConstructor:
    def test_add_ingredient_increases_counter(self):
        main_page = MainPage(self.driver)
        constructor_page = ConstructorPage(self.driver)

        main_page.go_to_constructor()

        initial_count = constructor_page.get_ingredient_count("ingredient_id")
        constructor_page.add_ingredient("ingredient_id")
        new_count = constructor_page.get_ingredient_count("ingredient_id")

        assert new_count == initial_count + 1
