"   ----List----    "
#Список это изменяемый тип данных .итерируемый. индексируемый и упорядоченный тип данных
#предназначенный для хранения элементов в строгом порядке

# list1 = [10,3,5,'Hello' , [1,2,3], (1,2),None , True , False]
# list1[0] # 10
# list1[3] # [1,2,3]
# list1[3][-1] # 3
# list1[-1] # False

# list2 = list('hello')
# print(list2) #['h','e','l','l','o']
# print(list(range(3,10,2))) #[3, 5, 7, 9]

"   ----Изменяемость----    "
# string = 'hello'
# res = string.upper()
# print(string) # 'hello'
# print(res) # 'HELLO'

# list = []
# list.append(1)
# list.append(2)
# list.append(3)
# print(list) # [1,2,3]

# a = 10
# b = 10
# print(id(a))
# print(id(b))

"   ----методы списков----  "
#append - метод который добавляет элемент в конец списка
# list = []
# list.append('hello')
# list.append(500)
# list.append([1,2,3])
# print(list)  #['hello', 500, [1, 2, 3]]

#remove - метод который удалет элемент из списка по значению , но только его первое вхождение этого элемента . выдаст ошибку ValueError,если такого элемента нет в списке

# list2 = ['hello',500 , 'world', 1000, 500]
# list2.remove('hello')
# print(list2) #[500, 'world', 1000, 500]

# # pop - метод который удаляет элемент из списка по индексу если этого индекса нет выдаст IndexError

# list3 = [10,20,30,40,50]
# list3.pop[]
# print(list3) #[10,20,30,40]
# list3.pop(1) # удаление по индексу 1
# print(list3) # [10,30,40]
# #так же метод pop возвращает удаленный элемент
# list4 = [10,20,30,40,50,]
# popped = list4.pop(0)
# print(list4) # [20,30,40,50]
# print(popped) # 10

# insert - метод который добавляет элемент в список по индексу
# list5 = [1,2,3,4,]
# list5.insert(0,'hello')
# print(list5) #('hello',1,2,3,4)


# list6 = [1,2,3,4,5,6,7,8,9,10]
# list6.reverse()
# print(list6)

# list7 = [1,2,3,4,5,6,7,8,9,10] 
# list8 = list7[::-1]
# print(list7)
# print(list8)

#reversed , reverse , [::-1]

#clear - метод чистит список
# list1 = [1,2,3]
# list1.clear()
# print(list1) #()

#count - считает количество элементов который передаем в метод в списке
# list1 = [1,2,3,4,5]
# list1.count(1) # 1

# list2 = ['hello','hello','hello']
# list2.count('hello') # 3

# list3 = [11,12,13]
# list3.count(1) # 0

#index - возвращает индекс данного элемента
# list2 = ['hello','world','makers']
# res = list2.index('hello')
# print(res) # 0

#sort - метод который сортирует по возрастанию
#если передать sort.(reverse)
# list3 = ['34'12'56'78'98']
# list3.sort()
# print(list3)

#copy - возвращает копию списка
list1 = [1,2,3]
list1 = list1.copy()
list2.append(4)
print(list1)
print(list2)

#extend - расширяет список другим списком
list3 = 