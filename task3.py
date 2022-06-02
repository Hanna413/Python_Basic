with open("text_3.txt", "r") as f3:
    content = f3.readlines()
my_list = []
for item in content:
    my_list.extend(item.replace('\n', '').split(' '))
my_dict = {}
i = 0
while i < len(my_list):
    my_dict[my_list[i]] = my_list[i + 1]
    i += 2
new_dict = {key: float(value) for key, value in my_dict.items()}
average_salary = sum(new_dict.values()) / len(my_dict)
print(f'Average salary is: {average_salary}')
low_salary = {key: val for key, val in new_dict.items() if val < 20000}
print('Employees with low salary:', end=' ')
print(*low_salary)


