"   ---- Области видимости / пространства имени ----   "
#LEGB - (local , enclosed, global, build-in)

#build-in встроенное пространство
#print , input , int , str

#global - глобальное пространство (наш файл)
#что бы посмотреть все глобальные переменные - globals

# a = 5
# b = 7
# print(globals())

# # enclosed - замкнутое пространство (находится между двумя пространствами)
# # локальное пространство , внутри которого есть еще одно локальное пространство

# def func():
#     var = 'замкнутая'
#     def inner_func():
#         var = 'локальная'
#         def inner_inner_func():
#             var = 'супер локальная переменная'
#             print(var)
#         inner_inner_func()
#         print(var)
#     inner_func()
#     print(var)
# func()
# print(var)

"local - локальное пространство (внутри функции)"

# a = 'hello'

# def func(a, b):
#     print('Global',globals()) # ('a':'hello','func':<function ...>)
#     print('Local',locals()) # ('a':10, 'b:50')

# func(10, 50)

# num1 = 10

# def func():
#     print(num1)

# func()


counter = 0

def increase_counter():
    global counter
    counter += 1
    print(counter)

increase_counter()
increase_counter()
increase_counter()
increase_counter()


def count(1):
    counter = 0

    def increase_counter():
        nonlocal counter
        counter += 1
        print(counter)

    for _ in range(i):
        increase_counter()

count(10)


def func():
    a = 10
    def inner_func():
        def inner_inner_func():
            nonlocal a
            a += 1
        inner_inner_func()
        print(a)
    inner_func()
func()