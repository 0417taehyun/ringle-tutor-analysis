def update_interests(tutors: list[dict], interests: dict[str, int]) -> None:
    for tutor in tutors:
        for interest in tutor["interests"]:
            if interest in interests:
                interests[interest] += 1
            else:
                interests[interest] = 1
