import requests  # type: ignore[import]

from src.core import get_settings

API_URL: str = get_settings().API_URL
AUTHORIZATION: str = get_settings().AUTHORIZATION


def get_tutors_information(
    page: int, API_URL: str, AUTHORIZATION: str
) -> list[dict]:
    response = requests.get(
        url=API_URL + str(page),
        params={"type": "all"},
        headers={"Authorization": f"Bearer {AUTHORIZATION}"},
    )

    tutors: list[dict] = response.json()["tutors"]
    return tutors
