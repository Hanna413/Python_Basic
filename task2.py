with open('text2.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.readlines()
    for ind, value in enumerate(content, 1):
        words = len(value.split())
        print(f'String {ind} contains {words} words.')
    print(f'Total number of strings: {ind}')
