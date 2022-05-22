def my_func(x, y):
    if x < 0 or y > 0:
        print('Перечитай условие')
    else:
        return x ** y


print(my_func(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))


def my_func2(x, y):
    if x < 0 or y > 0:
        print('Перечитай условие')
    else:
        base = x
        for _ in range(2, abs(y) + 1):
            x = x * base
        return 1 / x


print(my_func2(int(input('Введите положительное число: ')), int(input('Введите отрицательное число: '))))
