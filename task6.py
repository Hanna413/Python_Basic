a = int(input('Enter start number: '))
b = int(input('Enter goal number: '))
day = 1
goal = a
while goal < b:
    goal = goal + goal * 0.1
    day += 1
print(f'On the day {day}, the athlete reached the result - at least {b} km.')
