gain = int(input('Enter your gain: '))
cost = int(input('Enter your costs: '))

if gain > cost:
    print('Gain is more than costs! :)')
    profit = gain - cost
    profitability = profit / gain
    print(f'Profitability of your business is {profitability}.')
    number_employee = int(input('Enter number of employees: '))
    profit_per_employee = profit / number_employee
    print(f'Profit per each employee is {profit_per_employee}.')
else:
    print('Gain is less than costs... :(')

