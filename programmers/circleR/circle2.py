def solution(r1, r2):
    from math import ceil
    result = 0
    for x in range(1, r2 + 1):
        y1 = ceil(max(r1 ** 2 - x ** 2, 0) ** 0.5)
        y2 = int(max(r2 ** 2 - x ** 2, 0) ** 0.5)
        result += y2 - y1 + 1
    return result * 4