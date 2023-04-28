from collections import deque

def dfs(tickets, startIdx):
    answer = [tickets[startIdx][0]]
    d = deque()
    d.append(tickets[startIdx])
    visited = [0] * len(tickets)
    visited[startIdx] = 1
    
    while d:
        a = list(d.popleft())
        s = a[0]
        e = a[1]
        print(f"s : {s}, e: {e}")
        temp = []
        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[i][0] == e:
                temp.append(i)
        
        print(visited)
        temp.sort(key=lambda x: tickets[x][1])
        ti = 0
        # temp -> [0, 1]
        for t in temp:
            has = False
            for i, ticket in enumerate(tickets):
                if visited[i] != 1 and ticket[0] == tickets[t]:
                    has = True
            if has:
                ti += 1
        
        visited[temp[ti]] = 1

        if min(visited) != 1:
            answer.append(tickets[temp[ti]][0])
            d.append(tickets[temp[ti]])
        else:
            answer.append(tickets[temp[ti]][1])

    return answer

def solution(tickets):
    answer = []

    # 시작 인덱스 구하기
    start = []
    for i, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            start.append(i)
    
    start.sort(key=lambda x: tickets[x][1])  
        
    return dfs(tickets, start[0])  

print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))