def DFS(maps, x, y):

    maps[y][x] == 2
    count = 1

    if (x == len(maps[0]) - 2) and (y == len(maps[0]) - 2):
        return count

    if maps[y][x - 1] == 1:
        count += DFS(maps, x - 1, y)
    elif maps[y][x + 1] == 1:
        count += DFS(maps, x + 1, y) 
    elif maps[y + 1][x] == 1:
        count += DFS(maps, x, y + 1) 
    elif maps[y - 1][x] == 1:
        count += DFS(maps, x, y - 1)
    else:
        return -1

    return -1

def solution(maps):
    answer = 0
    
    # 상하좌우 벽 추가
    wMaps = [[0] * (len(maps[0]) + 2)]
    for m in maps:
        wMaps.append([0] + m + [0])
    wMaps.append([0] * (len(maps[0]) + 2))

    # start : (1, 1)   |   end : len(maps[0])
    answer = DFS(wMaps, 1, 1)
    print(wMaps)
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))