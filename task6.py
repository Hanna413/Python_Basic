goods = []
n = int(input('Сколько у Вас товаров? '))
i = 1
for _ in range(n):
    name = input('Введите имя товара: ')
    price = int(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    units = input('Введите единицу измерения количества: ')
    goods.append((i, {'название': name, 'цена': price, 'количество': quantity, 'eд': units}))
    i += 1
print(goods)
goods_dict = {}
names = []
prices = []
quantity = []
units = []
for i in range(0, len(goods)):
    names.append(goods[i][1].get('название'))
    prices.append(goods[i][1].get('цена'))
    quantity.append(goods[i][1].get('количество'))
    units.append(goods[i][1].get('eд'))
goods_dict['название'] = names
goods_dict['цена'] = prices
goods_dict['количество'] = quantity
goods_dict['eд'] = list(set(units))
print(goods_dict)
