import allure
from delayed_assert import expect


class TestUtils:

    @allure.step("Verify that the status code of the request is returning 200")
    def expect_status_code(self, endpoint_name, response, status_code):
        if response.status_code == status_code:
            expect(True)
        else:
            print(
                f"Expected status code: {status_code}, returned status code: {response.status_code} for endpoint '{endpoint_name}': {response.url}")
            expect(False)

    @allure.step("Verify that the response is returning as a non-empty list")
    def verify_is_non_empty_list(self, response):
        if isinstance(response.json(), list):
            if len(response.json()) >= 1:
                expect(True)
            else:
                print(f"An expected list is returning empty for this endpoint response: {response.url}")
                expect(False)
        else:
            expect(False)
            print(
                f"A list was expected from the response but a {type(response.json())} was returned for this endpoint: {response.url}")

    @allure.step("Verify that a specific key is returning as a certain data type")
    def verify_key_data_type_list(self, response, key, expected_data_type):
        for item in response.json():
            if isinstance(item[key], expected_data_type):
                expect(True)
            else:
                print(
                    f"The '{key}' key is expected to return as a {expected_data_type}, but returned as a {type(item[key])} data type from this endpoint: {response.url} and movie id: {item['id']}\n")
                expect(False)

    @allure.step("Create a new item and get the data of the new item")
    def get_created_movie_item(self, response):
        item_title = response.json()["title"]
        item_year = response.json()["year"]
        item_genre = response.json()["genre"]
        item_rating = response.json()["rating"]
        item_id = response.json()["id"]

        return {"item_title": item_title, "item_year": item_year, "item_genre": item_genre, "item_rating": item_rating,
                "item_id": item_id}

    @allure.step("Verify movie existence")
    def verify_movie_existence(self, response, item_title, item_year, item_genre, item_rating, item_id):
        if response.status_code == 200:
            new_movie = [{"title": item_title, "year": item_year, "genre": item_genre,
                          "rating": item_rating,
                          "id": item_id}]

            movie_found = response.json()

            if new_movie == movie_found:
                expect(True)
            else:
                print(f"The expected movie item: {new_movie}\n does not match the found movie with matching id: {movie_found} for this endpoint variation: {response.url}\n")
                expect(False)
        else:
            print(f"The endpoint {response.url} responded with status code {response.status_code}")
            expect(False)

    @allure.step("Verify movie does not exist")
    def verify_movie_non_existence(self, response):
        if response.status_code == 404:
            expect(True)
        elif response.status_code == 200:
            print(f"The endpoint {response.url} responded with status code {response.status_code} verifying that the movie item exists\n")
            expect(False)
        else:
            print(
                f"The endpoint {response.url} responded with status code {response.status_code}\n")
            expect(False)
