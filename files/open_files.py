"   ----Пакеты и модули ----  "
# module - любой файл с расширением .py
#import test
#print (test.a)

#from test import a
#print(a)

#package - набор модулей (в папке обязательно должен быть __init__.py)

"   ----Работа с файлами----  "
# open - функция, которая позволяет открыть файл в опереденном режиме
# r - read (только для чтения)
# w - write (только для перезаписи, каждый раз при открытии очищает файл)
# a - append (только для записи, добавляется в конец)
# x - создает файл, но если файл уже есть - ошибка
# b - бинарный вид

"   ----Read----    "
# file = open('test.txt')
# если такого файла нет - выйдет ошибка
# если не указать режим - откроется в режиме чтения

#print(dir(file))

#print("readable", file.readable()) #True
#print("writable", file.writable()) #False

#print(file.read()) # считывает от начала до конца
#print(file.read()) # '' потому что каретка в конце файла
#file.seek(0) # перенос каретки в начало ( на индекс 0)
#print(file.read())

#file.seek(5)
#print(file.read()) # считывает от начала до конца

#file.seek(0)
#print(file.read(5)) # 'Hello' считываем 5 символов
#print(file.read()) # '\nWorld\nMakers\s' считываем от 5 до конца

#file.seek(0)
#print(file.readline()) # 'Hello\n' считывает до \n
#print(file.readline()) # 'Hello\n' считывает до \n

#file.seek(0)
#print(file.readlines()) #['Hello\n', 'World\n', 'Malers\n']

#file.seek(10)
#print(file.tell()) #10

#file.read() # считает до конца ( на 10 индекс)
#print(file.tell()) #10

#print(file.name) # 'test.txt'
#print(file.closed) # False  возвращает булевое значение 
#file.close() # Важно закрывать файлы !!!
#print(file.closed) # True


"   ----Write----  "
file = open("new_file.txt", 'w')
# если файла нет - создает
# если есть - очищает


#print("readable", file.readable()) # False
#print("writable", file.writable()) # True

#file.read()

#file.write('Hello ')
#file.write('Makers') # Hello Makers


#file.writelines(['Hello', 'World']) # Hello MakersHelloWorld

#file.seek(0)
#file.write('AAA') 

file.close()

"   ----Append----  "
file = open('new_file2.txt','a')
#если файла нет - создается новый
#print("readable", file.readable()) # False
#print("writable", file.writable()) # True

#file.write('Hello')
#дозапись идет в конец файла (страрые данные не удаляются)

#file.seek(0)
#file.write('New')
#Все равно в конец дозапись


file.close()

"   ----Контекстный менеджер----  "

# try:
#     file = open('aaa.txt','w')
#     file.read()
# finally:
#     file.close()


with open('test.txt') as f:
    f.read()
    f.seek(0)
    f.read()
    print(f.closed) #False
# файл закрывается
print(f.closed) # True