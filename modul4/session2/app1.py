def get_age_mean() -> int:
    while True:
        try:
            numer_of_users = int(input("Cati participanti avem la sondaj?"))
        except ValueError:
            continue
        break
    age_sum = 0
    for user_number in range(numer_of_users):
        while True:
            try:
                age = int(input(f"Introduceti varsta participantului {user_number + 1}:"))
            except ValueError:
                continue
            break
        age_sum += age
    average = age_sum / numer_of_users
    return average

print(get_age_mean())