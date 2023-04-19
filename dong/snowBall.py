n, a, d = map(int, input().split())
ans = []
for i in range(0, n):
    ans.append(a)
    a *= d
print(ans)