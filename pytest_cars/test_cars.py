import pytest
import logging

logger = logging.getLogger("cars_tests")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        "test_search.log",
        mode="w",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 1),
        ("price", 5),
        ("price", 10),
        ("year", 3),
        ("year", 7),
        ("brand", 10),
        ("engine_volume", 5),
    ]
)
class TestCarsSearch:

    def test_search_cars(self, session, sort_by, limit):
        url = "http://127.0.0.1:8080/cars"

        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        logger.info(
            "Testing GET /cars with sort_by=%s, limit=%s",
            sort_by,
            limit
        )

        response = session.get(url, params=params)

        assert response.status_code == 200, (
            f"Expected status code 200, "
            f"got {response.status_code}. "
            f"Response: {response.text}"
        )

        cars = response.json()

        assert isinstance(cars, list), (
            "Response should be a list"
        )

        assert len(cars) == limit, (
            f"Expected {limit} cars, got {len(cars)}"
        )

        actual_values = [car[sort_by] for car in cars]

        assert actual_values == sorted(actual_values), (
            f"Cars are not sorted by {sort_by}"
        )

        logger.info(
            "Test passed: sort_by=%s, limit=%s, returned=%s cars",
            sort_by,
            limit,
            len(cars)
        )
