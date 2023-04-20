def solution(sequence):
    arr = [[0] * (len(sequence) + 1) for _ in range(2)]
    pulse = [[1, -1], [-1, 1]]

    for i in range(2):
        arr[i][0] = sequence[0] * pulse[i][0]
        for j in range(1, len(sequence)):
            arr[i][j] = max(sequence[j] * pulse[i][j % 2] + arr[i][j - 1], sequence[j] * pulse[i][j % 2])
    
    return max(max(arr[0]), max(arr[1]))



def solution2(sequence):

    # 1 부터 연속펄스 부분 수열을 곱한값 찾기 prefix sum 만들기 
    # maxV - minV 
    # 각각의 리스트에서 max()
    answer = 0
    prefixS = [0]
    for i in range(len(sequence)):
        pulse = 1 if i%2 ==0  else -1
        prefixS.append(prefixS[-1]+pulse*sequence[i])

    print(prefixS)
    return abs(max(prefixS) - min(prefixS))

print(solution2([2, 3, -6, 1, 3, -1, 2, 4]))