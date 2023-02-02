"----Строки----"
#Строки это неизменяемый тип данных  , предназначенный для хранения текста (последовательности символов)

string1 - 'строка в одинарных ковычках'
string2 - "строка в двойных ковычках"
string3 - "Sos 't' "
string4 - 'Study is "Makers Incubator" '
String5 - '''Многострочный 
текст, тут можно использовать 'любые' "кавычки" '''
String7 - 'Hello' +''+ 'world' # 'hello world'
String8 - 'hello' * 3 # 'hellohellohello'
String9 - 'hello' + str(1)

"----Экранизация строк----"
'\n' #пернос на новую строку
'\t' #отступ (табуляция)
print('hello\tworld')
'\\' # отображение бэк слэша \
'\'' # отображение '
'\"' # отображение "
'\r' # перенос каретки на начало строки
'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки

'hello\nworld'
#hello
#world

'hello\world'
#hello  world

'экранизация \\'
#экранизация \

'123456789\rhello'
#hello6789

"----Индексация----"
# индекс - порядковый номер символов в строке (начиная с 0)
'h e l l o'
#0 1 2 3 4

string - 'hello world'
print(string[0])
string[0] # 'h'
string[-1] # 'd'
string[-5] # ' '

# срез - часть строки
string[6:9] # 'wor'
string[0:5] # 'hello'
string[0:6] # 'hello '
string[:-6] # 'hello '
string[7:]  # 'hello world'
string[0:11:2] # 'hlowrd'

"----Форматирование строк----"
title = 'пирог'
price = 35
string = f'название: {title} , цена: {price}'
print(string)
#название: Пирог, цена: 35

format1 = 'Название: %s, цена: %s'
print(format1 % ('Яблоко','80'))

format2 = 'Название: (), цена: ()'
print(format2).format('Груша', 60)
#Название: Груша , цена: 60

"----Методы строк----"
#метод это функция которая принадлежит к определенному типу данных , обращаемся к ней через точку

print(dir(str)) #посмотреть все доступные методы для данного типа данных

'hello'.upper() # 'HELLO'
'hello'.lower() # 'hello'

'hello WORLD'.swapcase()   # 'HELLO world'
'hello'.swapcase()         # 'hElLo'
'hello world'.title()      # 'Hello World'
'hello world'.capitalize() # 'Hello world'

'hello'.center(11)  # '
'hello'.count('l')  # 1
'hello'.count('ll') # 2
'hello'.count('')   # 6

'hello world'.split()         # ['hello' , 'world']
' '.join(['hello' , 'world']) # 'hello world'
'hello world'.find('w')       #  индекс 6
'hello world'.rfind(o)        #  обратный индекс 7