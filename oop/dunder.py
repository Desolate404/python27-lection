# dunder (double underscore) - методы у которых 2 __ в начале и в конце
# магия в том, что мы их не вызываем напрямую

# class A:
#     def __new__(cls):
#         print('__NEW__')
#         return super().__new__(cls)
    
#     def __init__(self):
#         print("__INIT__")
#         pass

# A()
# __NEW__
# __INIT__

#__ new__ , __init__ - вызывается при создании обьекта

#print(dir(object))
#print(A.__dir__(A))
#__eq__ ==
#__ge__ >=
#__gt__ >
#__le__ <=
#__lt__ <
#__ne__ !=
#__add__ +
#__sub__ -
#__Floordiv__ /
#__truediv__ //
#__str__ str,print


#print(dir(int))
class A:
    pass
    #__str__ str,print

print(A())
#<__main__.A object at 0x7fe26db1ed30>
    
# print(A())

# class A:
#     def __str__(self) -> str:
#         return "Hello"
    
# print(A())
#Hello