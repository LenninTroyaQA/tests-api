import requests
from configuration.api_config import url
import allure
from test_utils.utilities.mock_test_data import title, year, genre, rating


class Base:

    @allure.step("Call the get movies list endpoint")
    def get_movies_list(self):
        response = requests.get(f"{url}/api/movies")

        return response

    @allure.step("Call the add movie to list endpoint")
    def add_movie_list(self):
        response = requests.post(f"{url}/api/movies", json={"title": title, "year": year, "genre": genre, "rating": rating})

        return response

    @allure.step("Call the get movie endpoint")
    def get_movie(self, movie_id):
        response = requests.get(f"{url}/api/movies/{movie_id}")

        return response

    @allure.step("Call the update movie endpoint")
    def update_movie(self, movie_id):
        response = requests.put(f"{url}/api/movies/{movie_id}", json={"title": "updated_title", "year": "updated_year", "genre": "updated_genre", "rating": "updated_rating"})

        return response

    @allure.step("Call the delete movie endpoint")
    def delete_movie(self, movie_id):
        response = requests.delete(f"{url}/api/movies/{movie_id}")

        return response
