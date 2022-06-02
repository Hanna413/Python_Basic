from googletrans import Translator

with open('text_4_en.txt', 'w', encoding='utf-8') as en_f4:
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        en_f4.write(Translator().translate(content, dest='ru').text)
