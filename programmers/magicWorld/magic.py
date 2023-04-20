def solution(storey):
    answer = 0
    a = str(storey)
    l = len(a)

    while not (int(a) in range(-9, 9)):
        if int(a[1]) > 4:
            try:
                v = abs(int(a[0]) + 1)
            except ValueError:
                v = abs(int(a[1]) + 1)
            answer += v
            v *= (10 ** len(a) - 2)
            #print(v)
            a = str(int(a) - v if int(a) > 0 else int(a) + v)
        else:
            try:
                v = abs(int(a[0]))
            except ValueError:
                v = abs(int(a[1]))
            answer += v
            v *= (10 ** len(a) - 2)
            a = str(int(a) - v if int(a) > 0 else int(a) + v)
    

    return answer

print(solution(int(input())))