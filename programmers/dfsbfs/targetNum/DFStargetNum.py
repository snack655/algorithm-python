def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers): # 리프 노드일 경우 -> len과 깊이가 같음.
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: 
            return 0
    else:
        answer += DFS(numbers, target, depth + 1) # 다음 단계의 노드로 재귀
        numbers[depth] *= -1    # 현재 단계의 노드를 -로
        answer += DFS(numbers, target, depth + 1)
        return answer

def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

print(solution([4, 1, 2, 1], 4))