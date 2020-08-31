from _datetime import datetime
import json

def get_path(path):
    path = f'{path}\log_path.json'
    def decorator_logger(function):
        def get_info(*args, **kwargs):
            date = datetime.today().replace(microsecond=0)
            new_function = function(*args, **kwargs)
            information = f'Дата и время {date}, функция {get_path.__name__}, аргументы: {args}, {kwargs}'
            with open('log_path.json', 'w', encoding='utf-8') as f:   # запись в файл
                json.dump(information, f, ensure_ascii=False, indent=2)
            print(f'Данные записаны в файл', 'log_path.json')
            return new_function
        return get_info
    print(f'Путь к файлу log_path.json:', path)
    return decorator_logger

input_path = input('Введите путь к логам ')
if __name__ == '__main__':
    @get_path (input_path)
    def logger(first_name, last_name):
        return first_name, last_name
    logger('Иван', 'Иванов')

