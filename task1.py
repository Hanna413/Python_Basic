class Date:

    @classmethod
    def str_to_num(cls, date):
        date_list = date.split("-")
        for i in range(0, len(date_list)):
            date_list[i] = int(date_list[i])
            i += 1
        return date_list

    @staticmethod
    def validation(date):
        date_list = Date.str_to_num(date)
        big_months = [1, 3, 5, 7, 8, 10, 12]
        if date_list[1] <= 0 or date_list[1] > 12:
            return "В году 12 месяцев"
        if date_list[1] == 2:
            if date_list[0] <= 0 or date_list[0] > 28:
                return "В феврале только 28 дней"  # сюда можно добавить проверку на високосность но я не стала
        elif date_list[1] in big_months:
            if date_list[0] <= 0 or date_list[0] > 31:
                return "В месяце может быть только 31 день и не может быть дня 0!"
        else:
            if date_list[0] <= 0 or date_list[0] > 30:
                return "В этом месяце только 30 дней и нет дня 0!"


print(Date.str_to_num('32-12-1999'))
print(Date.validation('32-12-1999'))
