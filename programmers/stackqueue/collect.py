def solution(s):
    answer = True
    stack = []
    for v in s:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        answer = False
    return answer

print(solution("(()("))