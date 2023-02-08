"   ----циклы----   "
# циклы - блок кода котрый отрабатывается несколько раз
#for - цикл который работает с итерируемыми объектами
#цикл заканчивает свою работу когда он доходит до последнего элемента в итерируемом объекте
#while - цикл , который работает до тех пор ,пока условие верно

# list1 = ['helllo', 10 , True , [1,2,3]]
# for element in list1:
#     print(element)

# string1 = 'hello world'
# for letter in string1:
#     print(letter)

# i = 1
# while i != 10:
#     print('hello', i)
#     i = i + 1

# i = 0
# while i:    # вообще ни разу не отоборажает , потому что 0 это False
#     print('hello world')
#     i = i + 1

"   ----Ключевые слова в цикле----  "
#break - полностью останавливает цикл
#continue - переход к следующей итерации

# for i in range (10):
#     if i == 3:
#         break
#     print(i)  # 0
#               # 1
#               # 2

# for i in range (10):
#     if i == 3:
#         continue
#     print(i) #0 1 2 3 4 5 6 7 8 9

list1 = [1,2,3,1,2,3]
list1.pop(0)
list1.pop(2)
print(list1)

list2 = [1,2,3,4,1,2,1,2,1]
while 1 in list2:
    list2.remove(1)
print(list2)