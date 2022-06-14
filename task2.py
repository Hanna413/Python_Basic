class MyError(Exception):
    def __init__(self, err_text):
        self.text = err_text


def divis_no_error(a, b):
    try:
        if b == 0:
            raise MyError('Нельзя делить на ноль!')
    except MyError as err:
        print(err)
    else:
        print(a / b)


divis_no_error(5, 0)
