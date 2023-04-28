def solution(arr):
    answer = [arr[-1]]
    for i in range(len(arr) - 1, -1, -1):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            arr.pop()
        else:
            arr.pop()
    return answer[::-1]

print(solution([1, 2]))