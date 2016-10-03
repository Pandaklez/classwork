import json
import urllib.request

json_string = """{"organisation": "Python Software Foundation",
                 "officers": [
                            {"first_name": "Guido", "last_name":"Rossum", "position":"president"},
                            {"first_name": "Diana", "last_name":"Clarke", "position":"chair"},
                            {"first_name": "Naomi", "last_name":"Ceder", "position":"vice chair"},
                            {"first_name": "Van", "last_name":"Lindberg", "position":"vice chair"},
                            {"first_name": "Ewa", "last_name":"Jodlowska", "position":"director of operations"}
                            ],
                "type": "non-profit",
                "country": "USA",
                "founded": 2001,
                "members": 244,
                "budget": 750000,
                "url": "www.python.org/psf/"}"""

data = json.loads(json_string)
#print(type(data))
#print(data)

for key in data:
    print(key, end = ' ')

d = {"John": 21, "Kate": 20, "Bill": 27}
json_string = json.dumps(d)
print(json_string)

# the same with arrays
arr = ['the', 'same']
json_string = json.dumps(arr)
print(type(json_string)) 
print(json_string)

user = "Pandaklez"
url = 'https://api.github.com/users/%s/repos' % user
response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
text = response.read().decode('utf-8')  # читаем ответ в строку
data = json.loads(text) # превращаем джейсон-строку в объекты питона
#print(len(data))  # можно распечатать, сколько у пользователя репозиториев
for i in data:
    print(i["language"]) # и распечатать названия всех репозиториев
