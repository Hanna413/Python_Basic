d = {}
with open('text_6.txt', 'r', encoding='utf-8') as f6:
    for line in f6:
        name, hours = line.split(':')
        my_l = ''.join([i if i in '1234567890' else " " for i in hours]).split()
        list_num = [int(i) for i in my_l if i != '']
        d[name] = sum(list_num)
print(d)
