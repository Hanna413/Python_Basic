def my_func(n1, n2, n3):
    list_num = [n1, n2, n3]
    max1 = list_num.pop(list_num.index(max(list_num)))
    max2 = max(list_num)
    return max1 + max2
