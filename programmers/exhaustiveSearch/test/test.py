def solution(answers):
    answer = []
    r1 = [1, 2, 3, 4, 5]
    r2 = [2, 1, 2, 3, 2, 4, 2, 5]
    r3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    arr = [[1, 0], [2, 0], [3, 0]]
    
    for i, v in enumerate(answers):
        if r1[i % len(r1)] == v:
            arr[0][1] += 1
        if r2[i % len(r2)] == v:
            arr[1][1] += 1
        if r3[i % len(r3)] == v:
            arr[2][1] += 1
    
    arr.sort(key=lambda x:-x[1])
    if sum([a[1] for a in arr]) == 0:
        return answer
    
    answer.append(arr[0][0])
    for i in range(1, len(arr)):
        if arr[i][1] == arr[0][1]:
            answer.append(arr[i][0])
        else: break
        
    return sorted(answer)

print(solution([1,3,2,4,2]))