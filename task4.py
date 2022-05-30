old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_dict = {}
for item in old_list:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1
result = [el for el in old_list if my_dict[el] == 1]
