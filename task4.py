user_words = input('Enter words separated by spaces: ').split(' ')
for ind, word in enumerate(user_words):
    print(ind, word[:10])
