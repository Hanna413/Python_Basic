def endless_count():
    sum_res = 0
    try:
        while True:
            for n in map(int, input('Введите числа через пробел: ').split()):
                sum_res += n
            print(sum_res)
    except ValueError:
        print(f'Сумма = {sum_res}, программа завершена из-за неверного ввода.')


endless_count()
