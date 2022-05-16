number = int(input('Enter your number: '))

max_number = 0

while number != 0:
    digit = number % 10
    number = number // 10
    if digit > max_number:
        max_number = digit


print(f'Maximum digit from your number is: {max_number} ')
