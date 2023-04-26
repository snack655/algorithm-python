def solution(sizes):
    arr = []
    for size in sizes:
        arr.append(sorted(size, reverse=True))
    print(arr)
    v1 = max([a[0] for a in arr])
    v2 = max([a[1] for a in arr])
    return v1 * v2

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))