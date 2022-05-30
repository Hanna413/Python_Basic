from functools import reduce


def my_multiply(a, b):
    return a * b


result = reduce(my_multiply, [num for num in range(100, 1001)])
print(result)
