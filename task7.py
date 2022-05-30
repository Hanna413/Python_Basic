def my_fact(number):
    fact_n = 1
    if number != 0:
        for i in range(1, number + 1):
            fact_n *= i
            yield fact_n


for el in my_fact(int(input('Введите число: '))):
    print(el)
