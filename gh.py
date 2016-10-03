import urllib.request as ur
import json

ask = input('Введите ваш поисковый запрос:')
page = ur.urlopen('https://yandex.ru/suggest/suggest-endings?part=' + ask)
data = page.read().decode('utf-8')
print(data)
text = json.dumps(data, indent = 1, ensure_ascii = False)
print(type(text))
