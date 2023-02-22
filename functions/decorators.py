"   ----Декоратор----   "
# декоратор - функция высшего порядка, которая нужна чтобы расширять функционал другой функции, не меняя ее

# def decorator(func):
#     def wrapper():
#         print("Функция вызывается")
#         func()
#         print("Функция завершила работу")
#     return wrapper

# def func():
#     print('hello')

# res = decorator(func)
# print(res)
# <function decorator.<locals>.wrapper at 0x7f843c426310>
#Функция вызывается
#Функция завершила работу

"   ----Синтактический сахар----"
# def decorator(func):
#     def wrapper():
#         print("Функция вызывается")
#         func()
#         print("Функция завершила работу")
#     return wrapper

# @decorator  #func = decorator(func)
# def func():
#     print('hello')

# func()
#Функция вызывается
#hello
#Функция завершила работу
#<function decorator.<locals>.wrapper at 0x7f843c426310>


# @decorator
# def  func(string):
#     print(string)

# func("hello")


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(args, kwargs)

from datetime import datetime

def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f'функция отработала за {end-start}')
    return wrapper

@timer
def func(count):
    for i in range(count):
        print(i)

func(10)

#<b>text/b> - жирный
#<i>text</i> курсив

def bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

@bold
@italic
def func(string):
    return f'Hello {string}'
# func = bold(italic(func))

print(func('Makers'))