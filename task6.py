from itertools import count, cycle

n = int(input('Введите стартовое число: '))
for i in count(n):
    print(i)
    if i > n + 12:
        break

for i in cycle(input('Введите что-либо через пробел, для выхода нажмите q: ').split()):
    print(i)
    quit1 = input()
    if quit1 == 'q':
        break
