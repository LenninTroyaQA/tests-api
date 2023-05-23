import pytest
from test_utils.factory import Factory


@pytest.fixture()
def new_movie():
    return Factory.test_utils.get_created_movie_item(Factory.base.add_movie_list())
