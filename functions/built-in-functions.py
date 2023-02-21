"   ----Встроенные функции----    "
#enumerete - фуекция которая принимает последовательность и возвращает генератор, где элементы генератора

# string = 'hello'
# enum = enumerate(string)
# print(enum)   #<enumerate object at 0x7faf36b25500>
# print(list(enum))  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

# string = 'world'
# enum = enumerate(string, 5)
# print(list(enum))
#[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
#[(5, 'w'), (6, 'o'), (7, 'r'), (8, 'l'), (9, 'd')]

#дан список с числами,умножте на 2 все числа под нечетным индексом, умножьте на 3 все числа под индексом кратным 3
# list1 = [1,4,78,3,7,0,4,2,7]
# for ind in range(len(list1)):
#     element = list1[ind]
#     if ind % 2: # ind % 2 != 0
#         list1[ind] = element * 2
#     if ind % 3 == 0: # not ind % 2
#         list1[ind] = element * 3

# print(list1)  # [3, 8, 78, 9, 7, 0, 12, 4, 7]

# list1 = [1,4,78,3,7,0,4,2,7]
# for ind, element in enumerate(list1):
#     if ind % 2:
#         list1[ind] = element * 2
#     if ind % 3 == 0:

#создайте словарь где ключом будет порядковый номер буквы в алфавите а значением буква

# word = 'python'
# py_dict = {index+1: word[index] for index in range(len(word))}
# print(py_dict)

# import string

# alphabet = string.ascii_lowercase
# alphabet_dict = {i+1: letter for i, letter in enumerate(alphabet)}
#print(dict(enumerate(string,1)))

# zip
# list1 = [1,2,3,4,5]
# list2 = 'abcdefg'
# list3 = [0.5,0.3,0.6]

# print(list(zip(list1,list2,list3)))
#[(1, 'a', 0.5), (2, 'b', 0.3), (3, 'c', 0.6)]


"   ----Функция высшего порядка----  "
#это функция , которая :
# принимает в аргументы другую функцию ( функцию как объект)
#возвращает функцию 
#создает внутри функцию
#вызывает внутри себя функцию


#### map - принимает в аргументы функцию и итерируемые объект, возвращает она генератор в котором все элементы - результат принимаемой функции в которую передали элементы последовательности

# mapped = map(int, ['1','2','3'])
# print(mapped) #<map object at 0x7fdab5326dc0>
# print(list(mapped)) #[1, 2, 3]

#дан список с числами , создайте новый список где элементы - число из списка +1 используя map
# list1 = [1,2,3,4]
# res =  [2,3,4,5]


# list1 = [1, 2, 3, 4]
# res = list(map(lambda x: x+1 if x < 5 else x, list1))
# print(res) # [2, 3, 4, 5]


### filter - функция принимает в аргементы функцию в итерируемый объект , возвращает генератор , в котором элементы из последовательности прошедшие фильтр (функция вернула True)

# list1 = [-3,7,0,34,-23,435,10]
# def is_positive(i):
#     return i > 0

# print(list(filter(is_positive, list1)))
#[7, 34, 435, 10]
#print(list(filter(lambda i: i>0,list1)))
#[7, 34, 435, 10]


#дан список со строками , оставьте только те строки , которые начинаются с большой буквы
# list1 = ['Hello','world','MAKERS']
# # res = ['Hello','MAKERS']
# list1 = ['Hello', 'world', 'MAKERS']
# res = [i for i in list1 if i[0].isupper()]
# print(res) # ['Hello', 'MAKERS']

### reduce - Функция которая импортируется из модуля functools.
#тоже принимает функцию и итерируемый обьект,возвращает один результат

# from functools import reduce

# list1 = [2,4,6,3,65,8]

# def mul(x,y):
#     return x*y
# res = reduce(mul, list1)
# print(res) # 2*4*6*3*65*8

# string = 'hello'
# print(reduce(lambda x,y: x+'$'+y, string))
# h$e$l$l$o
# x='h', y='e' -> 'h$e'
# x='h$e', y='l' -> 'h$e$l'
# x='h$e$l', y='l' -> 'h$e$l$l'
# x='h$e$l$l', y='o' -> 'h$e$l$l$o'

#['hello','world','makers','bootcamp']
#выведите самое длинное слово с помощью reduce

from functools import reduce

words = ['hello', 'world', 'makers', 'bootcamp']
res = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print(res) # 'bootcamp'