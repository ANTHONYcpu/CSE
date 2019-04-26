import csv


def validate(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False