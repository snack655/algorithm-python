
def solution(sequence, k):
    start = 0
    end = len(sequence) - 1
    answer= []

    while not ((end - start) < 0):
        result = getSum(start,end,sequence)
        
        if (result == k):
            answer.append([start,end])
            print([start,end])
            break
        elif (result - k > sequence[end]):
            end -= 1
        else:
            start += 1
    
    return answer

def getSum(start,end,sequence):
    sum = 0
    for i in range(start,end+1):
        sum += sequence[i]
    return sum

print(solution([1, 1, 1, 2, 3, 4, 5],5))
