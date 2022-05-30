import sys


def my_salary():
    try:
        hs, per_hour, award = map(float, sys.argv[1:])
        print(f"Your salary is {hs * per_hour + award}")
    except ValueError:
        print("Only numbers allowed")


print(my_salary())
