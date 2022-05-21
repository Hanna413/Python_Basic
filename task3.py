# Через list

number_month = int(input('Enter number from 1 to 12: '))
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
print(f'Your month is {month_list[number_month - 1]}')

# Через dictionary
number_month = int(input('Enter number from 1 to 12: '))
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
print(f'Your month is {month_dict.get(number_month)}')
