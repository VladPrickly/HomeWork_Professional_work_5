import types
import os
import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        res = old_function(*args, **kwargs)
        filename = 'main_task3.log'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'Дата запуска программы - {datetime.date.today()}\n'
                    f'Время запуска программы - {datetime.datetime.now().strftime("%H:%M:%S")}\n'
                    f'Название функции - {old_function.__name__}\n'
                    f'Передаваемые аргументы - {args, kwargs}\n'
                    f'Возвращаемое значение - {res}\n\n\n')

        return res
    return new_function


@logger
def flat_generator(list_of_lists):
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            yield list_of_lists[i][j]


list_of_lists_1 = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]

print(next(flat_generator(list_of_lists_1)))



