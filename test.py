from functools import reduce
words = ['hello', 'world', 'makers', 'bootcamp']
res = reduce(lambda x,y:x if len(x) > len(y) else y, words)