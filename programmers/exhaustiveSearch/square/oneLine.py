def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)