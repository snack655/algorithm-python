def solution(sequence, k):
    answer = []
    slist = []
    for i in range(0, len(sequence)):
        for j in range(i, len(sequence)):
            if getSum(sequence, i, j) == k:
                slist.append([i, j])
    slist.sort(key=lambda x: (x[1]-x[0], x[0]))
    return slist[0]
            
def getSum(sequence, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += sequence[i]
    return sum

print(solution([1, 1, 1, 2, 3, 4, 5], 5))