def solution(sequence, k):
    answer = []
    slist = []
    for i in range(0, len(sequence)):
        for j in range(i, len(sequence)):
            if getSum(sequence, i, j) == k:
                slist.append([i, j])
                
    if len(slist) == 1:
        return slist[0]
    else:
        valueList = list(map(getMin, slist)) # [1, 0, 0]
        idxs = []
        for i in range(0, len(valueList)):
            if valueList[i] == min(valueList):
                idxs.append(i)
        if len(idxs) == 1:
            return slist[idxs[0]]
        else:
            minList = []
            for i in idxs:
                minList.append(slist[i]) # [[5, 5], [6, 6]]
            minList.sort(key=lambda x:x[0])
            return minList[0]
            
def getSum(sequence, start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += sequence[i]
    return sum

def getMin(values):
    return values[1] - values[0]

print(solution([2, 2, 2, 2, 2], 6))