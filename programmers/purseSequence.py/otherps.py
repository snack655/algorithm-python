def solution(sequence):
    dp = [[0] * (len(sequence) + 1) for _ in range(2)]
    pulse = [[1, -1], [-1, 1]]

    for i in range(2):
        dp[i][0] = sequence[0] * pulse[i][0]
        for j in range(1, len(sequence)):
            dp[i][j] = max(sequence[j] * pulse[i][j % 2] + dp[i][j - 1], sequence[j] * pulse[i][j % 2]) # (-3) + 2 VS -3 -> 2, -1
    
    return (max(max(dp[0]), max(dp[1])))

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
    