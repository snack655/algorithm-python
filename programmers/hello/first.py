def solution(scores):
    answer = 0

    isLow = False 
    for i in range(1, len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            answer = -1
            isLow = True
    
    if not isLow:
        nSum = scores[0][0] + scores[0][1]
        
        scores = list(map(sum, scores))
        scores.sort(reverse=True)
        answer = scores.index(nSum) + 1

    return answer

print(solution([[0, 0],[1,4],[3,2],[3,2],[2,1]]))
print(solution([[4, 2], [0, 0],[3,2],[3,2],[2,1]]))