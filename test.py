import json

#Сериализация - перевод из python в json
#dump
#десериализация - перевод из json в python
#load

#dump
#dumps - функция,которая переводит python obj
#load - 
#loads - функция, которая переводит json строку в python обьект

# python_list = [1,2,3]
# json_list = json.dumps(python_list) # [1,2,3]
# print(type(json_list)) # "[1,2,3]"

# json_dict = '{"a":1, "b":2}'
# python_dict = json.loads(json_dict)

# print(type(json_dict)) #str
# print(type(python_dict)) # dict

list_ = [
    1,2,3,
    4,5,
    (1,2,3),
    ('6':1),
    'hello',
    True,False,None
]

with open("test.json", "w") as file:
    json,dump(list_, file)


with open("test.json", "r") as file:
    res = json.load(file)

print(res)
