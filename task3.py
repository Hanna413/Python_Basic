class IfDigits(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


def checking():
    list_of_numbers = []
    obj = input('Введите число или наберите "stop" для выхода: ')

    while obj != 'stop':
        try:
            obj = int(obj)
        except ValueError:
            pass
        try:
            if not isinstance(obj, int):
                raise IfDigits('Не число!')
        except IfDigits as err:
            print(err)
        else:
            list_of_numbers.append(obj)
        finally:
            obj = input('Введите число: ')
    print(list_of_numbers)


checking()
