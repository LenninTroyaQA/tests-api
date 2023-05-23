import allure
from delayed_assert import delayed_assert
from test_utils.factory import Factory
import pytest


@pytest.mark.delete_movie
class TestDeleteMovie:

    @allure.title("Verify status code is returning 200")
    def test_017_delete_movie_verify_status_code(self, new_movie):
        Factory.test_utils.expect_status_code("Delete movie", Factory.base.delete_movie(new_movie["item_id"]), 204)
        delayed_assert.assert_expectations()

    @allure.title("Verify that a movie item was deleted correctly")
    def test_018_delete_movie_verify_movie_item_deleted(self, new_movie):
        new_movie_id = new_movie["item_id"]
        allure.step("Verify that a new movie was created")
        Factory.test_utils.verify_movie_existence(Factory.base.get_movie(new_movie_id), new_movie["item_title"],
                                                  new_movie["item_year"], new_movie["item_genre"],
                                                  new_movie["item_rating"], new_movie["item_id"])

        allure.step("Verify that the new movie created was deleted correctly")
        Factory.base.delete_movie(new_movie_id)
        Factory.test_utils.verify_movie_non_existence(Factory.base.get_movie(new_movie_id))
        delayed_assert.assert_expectations()
