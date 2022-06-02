with open('new_file.txt', 'w+') as f1:
    data = input('Enter your string: ')
    while data:
        f1.write(f'{data}\n')
        data = input('Enter your string: ')
