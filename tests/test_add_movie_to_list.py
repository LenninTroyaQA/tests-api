import allure
from delayed_assert import delayed_assert
from test_utils.factory import Factory
import pytest


@pytest.mark.add_movie_to_list
class TestAddMovieToList:

    @allure.title("Add a movie to the list and verify status code is returning 200")
    def test_005_add_movie_to_list_verify_status_code(self):
        Factory.test_utils.expect_status_code("Add move to list", Factory.base.add_movie_list(), 201)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the title, year, genre, and rating are the same as inputted")
    def test_006_add_movie_to_list_verify_data_inputted(self, new_movie):
        Factory.test_utils.verify_movie_existence(Factory.base.get_movie(new_movie["item_id"]), new_movie["item_title"], new_movie["item_year"], new_movie["item_genre"], new_movie["item_rating"], new_movie["item_id"])
        delayed_assert.assert_expectations()

    @allure.title("Verify that the new movie created has the 'year' key returning as an int data type")
    def test_007_add_movie_to_list_verify_year_key_data_type(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "year", int)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the new movie created has the 'rating' key returning as a float data type")
    def test_008_add_movie_to_list_verify_rating_key_data_type(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "rating", float)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the new movie created has the 'title' key returning as a string data type")
    def test_009_add_movie_to_list_verify_title_key_data_type(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "rating", str)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the new movie created has the 'genre' key returning as a string data type")
    def test_010_add_movie_to_list_verify_genre_key_data_type(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "genre", str)
        delayed_assert.assert_expectations()

    @allure.title("Verify that the new movie created has the 'id' key returning as a string data type")
    def test_011_add_movie_to_list_verify_id_key_data_type(self, new_movie):
        Factory.test_utils.verify_key_data_type_list(Factory.base.get_movie(new_movie["item_id"]), "id", str)
        delayed_assert.assert_expectations()