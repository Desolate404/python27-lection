# #дан список из чисел nounse target найти два числа из nounce которые в сумме дают target выведите индексы этих чисел
# nounce = [2,8,15,4,3]target = 11
# res = [1,4]

nounce = [3, 6, 3]
target = 6

res = {}

for i, num in enumerate(nounce):
    summa = target - num
    if summa in res:
        res = [res[summa], i]
        break
    res[num] = i

print(res) # [1, 4]
