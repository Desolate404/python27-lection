'=========================JSON============================='

# JavaScript Object Notatio - единый фоормат, в котором могут храниться только те типы данных, которые есть во всех языках, поддерживающие json

# числа int, float
# строки str
# словари dict
# булевые значения True, False
# списки list
# пустое значение None

import json

# сериализация - перевод из python в json
# dump
# dumps - функция которая переводит python обьект в json строку

# десериализация - перевод из json в python
# load
# loads - функция которая переводит json строку в python обьект

# print(dir(json))

python_list = [1,3,4]
json_list = json.dumps(python_list)
print(type(python_list)) # list
print(type(json_list))  # str

print(python_list) #  [1,3,4]
print(json_list)   # '[1,3,4]

json_dict = '{"a":1, "b":2}'
python_dict = json.loads(json_dict)

print(type(json_dict))  # str
print(type(python_dict)) # dict


list_ = [
    1,2,3,
    4.6,
    (1,2,3),
    'hello',
    True, None,
    {'A':1}
    # {1,2} TypeError: Object of type set is not JSON serializable
]

# Сериализация

with open("test.json", "w") as file:
    json.dump(list_, file)

# Десериализация

with open('test.json', 'r') as file:
    res = json.load(file)

print(res) # [1, 2, 3, 4.6, [1, 2, 3], 'hello', True, None, {'A': 1}]