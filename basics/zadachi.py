### 3 ###
# name_of_list = ['Helloworld!'] 
# string = name_of_list[0]

# len_ = len(string)

# if len_ % 2 == 0:
#     one = string[:len_ // 2]
#     sec = string[len_ // 2:]
# else:
#     one = string[:(len_ // 2) + 1]
#     sec = string[(len_ // 2) + 1:]

# new_list = list(sec) + list(one)
# print(new_list)

### 13 ###
# x = input()
# list_ = x.split(',')
# list_.sort()
# print(list_)


### 18 ###
# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = []

# for i in range(step):
#     new_list.append(list_[i::step])

# print(new_list)

### 21 ###
# str_list = ['abc', 'xyz', 'aba', '1221']
# new_list = []
# for i in str_list:
#     if i[0] == i[-1]:
#         res = str_list.index(i)
#         new_list.append(res)
# print(new_list)

### 22 ###
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = lists[0]
# min_list = lists[0]
# for i in lists:
#     if len(i) > len(max_list) and len(i) >= 0:
#             max_list = i
#     if len(i) < len(min_list) and len(i) >= 0:
#             min_list = i
# if len(max_list) > 1:
#     print(f'max_list {max_list}')
#     print(f'min_list {min_list}')
# else:
#     print(f'max_list {max_list}')
#     print(f'min_list {None}')

### 26 ###
# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]

# res = []
# res2 = []

# for color in colors1:
#     if color not in colors2:
#         res.append(color)

# for color in colors2:
#     if color not in colors1:
#         res2.append(color)

# print(res,res2)

### 29 ###
# list_ = [1, 2, 3]

# for x in list_:
#     for y in list_:
#         for z in list_:
#             if x != y and y != z and z != x:
#                 print((x, y, z))

### 30 ###
# K = 3
# matrix = []

# for i in range(K):
#     matrix.append([])

#     for j in range(K):
#         matrix[i].append(0)

# print(matrix)

### 31 ###
# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# res = []
# for i in colors:
#     res.append(i[::-1])
# print(sorted(res, key = len))

### 32 ###
# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step

# while i <= len(list_):
#     list_.insert(i, element)
#     i = i + step + 1
# print(list_)

### 33 ###
# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# max_ = max([x for x in lists], key = sum)
# print(max_)

### 35 ###
# list_ = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# list_[0: 5] = ["".join(list_[0: 5])]
# # print(["".join(list_[0: 5])])
# print(list_)
####
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# # ['abcd', 'e', 'f', 'g']

# for let in chars:
#     for let2 in chars[1:]:
#         if merge_from == let and merge_to == let2:
#             index1 = chars.index(let)
#             index2 = chars.index(let2)

# chars[index1: index2 + 1] = ["".join(chars[index1: index2 + 1])]
# print(chars)