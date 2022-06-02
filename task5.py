with open('text_5.txt', 'w') as f5:
    f5.write(input('enter numbers: '))
with open('text_5.txt', 'r') as f5:
    my_list = f5.read().split(' ')
num_list = map(float, my_list)
print(sum(list(num_list)))
