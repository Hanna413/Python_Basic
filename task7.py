import json

with open('task_7.json', 'w', encoding='utf-8') as dest_f:
    with open('text_7.txt', 'r', encoding='utf-8') as src_f:
        dict_main = {}
        for line in src_f:
            # my_list = line.split()
            dict_main[line.split()[0]] = float(line.split()[2]) - float(line.split()[3])
            avrg_profit_list = []
            for i in dict_main.values():
                if i > 0:
                    avrg_profit_list.append(i)
        json.dump([dict_main, {'average_profit': sum(avrg_profit_list) / len(avrg_profit_list)}], dest_f,
                  ensure_ascii=False)
