import allure
from delayed_assert import delayed_assert
from test_utils.factory import Factory
import pytest


@pytest.mark.get_movies_list
class TestGetMoviesList:

    @allure.title("Verify status code is returning 200")
    def test_001_get_movies_list_verify_status_code(self):
        Factory.test_utils.expect_status_code("Get movies list", Factory.base.get_movies_list(), 200)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the response is returning as a non-empty list")
    def test_002_get_movies_list_verify_response_is_returning_a_non_empty_list(self):
        Factory.test_utils.verify_is_non_empty_list(Factory.base.get_movies_list())
        delayed_assert.assert_expectations()

    @allure.title("Verify that the title key is returning as a string")
    def test_003_get_movies_list_verify_title_key_returns_string(self):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movies_list(), "title", str)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the year key is returning as an int")
    def test_004_get_movies_list_verify_year_key_returns_int(self):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movies_list(), "year", int)
        delayed_assert.assert_expectations()
