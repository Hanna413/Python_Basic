def my_division(num1, num2):
    return num1 / num2


try:
    print(my_division(int(input('Enter 1st number: ')), int(input('Enter 2nd number: '))))
except ZeroDivisionError:
    print("You can't divide by zero")
