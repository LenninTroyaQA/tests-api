import allure
from delayed_assert import delayed_assert
from test_utils.factory import Factory
import pytest


@pytest.mark.get_movie
class TestGetMovie:

    @allure.title("Verify status code is returning 200")
    def test_012_get_movie_verify_status_code(self, new_movie):
        Factory.test_utils.expect_status_code("Get movie", Factory.base.get_movie(new_movie["item_id"]), 200)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the title key is returning as a string")
    def test_0013_get_movie_verify_title_key_returns_string(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "title", str)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the year key is returning as an int")
    def test_0014_get_movie_verify_year_key_returns_int(self,new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "year", int)
        delayed_assert.assert_expectations()
