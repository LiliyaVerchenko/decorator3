from _datetime import datetime
import json

def decorator_logger(function):
    def get_info(*args, **kwargs):
        date = datetime.today().replace(microsecond=0)
        new_function = function(*args, **kwargs)
        information = f'Дата и время {date}, функция {decorator_logger.__name__}, аргументы: {args}, {kwargs}'
        with open('logger.json', 'w', encoding='utf-8') as f:   # запись в файл
            json.dump(information, f, ensure_ascii=False, indent=2)
        print(f'Данные записаны в файл', 'logger.json')
        return new_function
    return get_info

@decorator_logger
def logger(first_name, last_name):
    return first_name, last_name

logger('Иван', 'Иванов')


