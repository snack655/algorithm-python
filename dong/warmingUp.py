print([False] * 5)
print([False] for _ in range(5))
print([[False] for _ in range(5)])
print('*' * 30)

print([0]*5)
print([0 for i in range(5)])
print([0] for _ in range(5))
print([[0] for _ in range(5)])
print('*' * 30)

n = 4
graph = [[0 for j in range(n)] for i in range(n)]
print(graph)

# 어떤 결과가 나올지 작성해 보시오.
graph = [ [0] * 4 for _ in range(4)] 
print(graph)

# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

