import allure
from delayed_assert import delayed_assert
from test_utils.factory import Factory
import pytest


@pytest.mark.update_movie
class TestUpdateMovie:

    @allure.title("Verify status code is returning 200")
    def test_015_update_movie_verify_status_code(self, new_movie):
        Factory.test_utils.expect_status_code("Update movie", Factory.base.update_movie(new_movie["item_id"]), 200)
        delayed_assert.assert_expectations()

    @allure.title("Verify that a movie item was updated correctly")
    def test_016_update_movie_verify_movie_item_updated(self, new_movie):
        new_movie_id = new_movie["item_id"]
        allure.step("Verify that a new movie was created")
        Factory.test_utils.verify_movie_existence(Factory.base.get_movie(new_movie_id), new_movie["item_title"],
                                                  new_movie["item_year"], new_movie["item_genre"],
                                                  new_movie["item_rating"], new_movie["item_id"])

        allure.step("Verify that the new movie created was updated correctly")
        Factory.base.update_movie(new_movie_id)
        Factory.test_utils.verify_movie_existence(Factory.base.get_movie(new_movie_id), "updated_title",
                                                  "updated_year", "updated_genre",
                                                  "updated_rating", new_movie_id)
        delayed_assert.assert_expectations()
