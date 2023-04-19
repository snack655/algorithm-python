import itertools 

def toInt(x):
    return x[0] * 100 + x[1] * 10 + x[2]

str = input()
arr = list(map(int, list(str[str.index('[') + 1:str.index(']')].replace(', ', ''))))
k = int(str.split(',')[-1])

comb = list(itertools.permutations(arr, len(arr)))
arr2 = list(map(toInt, comb))
arr2 = list(filter(lambda x: x > k, arr2))

print(min(arr2) if len(arr2) != 0 else -1)