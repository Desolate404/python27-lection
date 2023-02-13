"   ----Comprehansions----    "
#Генераторь, с помощью которого можно создавать последовательность используя цикл for

# list1 = []
# for i in range(1, 11):
#     list1.append(i)
# #list1 = [1,2,3,4,5,6,7,8,9,10]

# list1 = [1 for i in range(1,11)]
# print(list1) #[1,2,3,4,5,6,7,8,9,10]

#результат for элемент in последовательность
#результат for элемент in последовательность if фильтр

# comprehansion = (i for i in range(1,4))
# print(comprehansion) #<generator object <genexpr> at 0x7fa82b35b660>

#Генератор - итерируемый обьект, который не хранит в себе полностью все элементы последовательности ,а генерирует их когда требуется
#print(next(comprehansion))

#next - функция которая принимает в себя генератор, запрашивает следующий элемент у генератора и возвращает его

# comprehansion = (i for i in range(1,4))
# print(list(comprehansion)) # [1,2,3]
# print(list(comprehansion)) # []

# list1 = [1,2,3]
# itera = iter(list1)
# while True:
#     try:
#         print(next(itera))
#         break
#     except StopIteration:
#         break

"   ----Синтактический сахар ----   "
#list comprehansion
#list_compr = [i for i in 'hello']
#print(list_compr)
#['h','e','l','l','o']

#dict_compr = {i:str(i) for i in range (1,11)}
#print(dict_compr) #{1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# Фильтр
# string = 'Hello World'
# res = [i for i in string if i.islower()]
# print(res) #['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

# res = []
# for i in string:
#     if i.islower():
#         res.append(i)
# print(res) #['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']

#создайте список состоящий из чётных чисел от 1 до 10
# even_ = [num for num in range(1,11) if num % 2 == 0]
# print(even_)

# list_of_even_nums = []
# for num in range(1,11):
#    if num % 2 == 0:
#        list_of_even_nums.append(num)

# создайте сиписок из чисел от 1 до 10 умноженные на 100 при этом использовать только range(1,11)
# res = [i*100 for i in range(1, 11)]
# print(res) # [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#с помощью comprehansion создайте список состоящий из 5 строк 'hello'
#res = ['hello' for _ in range(5)]
#print(res) #['hello', 'hello', 'hello', 'hello', 'hello']

#создайте список с именами с помощью comprehansion 
# users = ['test1','test2','test3',]
# #['hello test1','hello test2','hello test3']
# strings = ['hello ' + i for i in users]
# print(strings)

#создать список в списке

# [
#     [1],
#     [1],[2],
#     [1],[2],[3],
#     [1],[2],[3],[4]
#     [1],[2],[3],[4],[5]
# ]
# lists_ = [[i for i in range(1, x+1)] for x in range(1, 6)]
# print(lists_)

# list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# res = [1,2,3,4,5,6,7,8,9,10,11,12]
# res = [i for inner_list in list1 for i in inner_list]
# for inner_list in list1:
#     for i in inner_list:
#         res.append(i)
# print(res)

# [1,2,3,4]
# ['не четное','четное','не четное','четное']
# res = ['четное' if i%2==0 else 'не четное' for i in range(1,7)]
# print(res)

# dict1 = {'a':1,'b':2,'c':3}
# #{1:'a',2:'b',3:'c'}
# dict2 = {value:key for key, value in dict1.items()}
# print(dict2)

#{1:[1], 2:[1,2], 3:[1,2,3], 4:[1,2,3,4]}
# list_of_lists = {i:[num for num in range(1, x+1)] for x in range(1, 5)}
# print(list_of_lists)
# {[i for i in range(1, x+1)] for x in range(1, 6)}

# set comprehantion
# set_comp = (x for x in range(10))
# print((1,True,'hello',10,1))
#(1, True, 'hello', 10, 1)
#1 == True
#0 == False
