from collections import Counter

from src.api import get_tutors_information
from src.core import get_settings
from src.util import update_interests

API_URL: str = get_settings().API_URL
AUTHORIZATION: str = get_settings().AUTHORIZATION


if __name__ == "__main__":
    interests: dict = {}

    for page in range(1, 65):
        tutors = get_tutors_information(page, API_URL, AUTHORIZATION)
        update_interests(tutors, interests)

    # Get Top 10 tutors' interests
    print(Counter(interests).most_common()[:10])
