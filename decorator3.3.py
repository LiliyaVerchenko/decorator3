import requests
import json
from decorator_path_3_2 import input_path, get_path

WIKI_URL = 'https://ru.wikipedia.org/wiki/'
@get_path(input_path)
class CountryWiki:
    # WIKI_URL = 'https://ru.wikipedia.org/wiki/'
    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        country_url = {}
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common'].replace(' ', '_')  # получаем название страны
        country_link = f'{WIKI_URL}{country}'    # получаем ссылку на страницу wiki
        country_url[country] = country_link      # записываем словарь

        return country_url


data = CountryWiki('countries.json', 0)
with open('country_link.json', 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False, indent=2)
print('Ссылки по каждой стране успешно сохранены в файл "country_link.json"')

# C:\Users\Константин\PycharmProjects\Decorators3