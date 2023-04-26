def solution(genres, plays):
    # 속한 노래가 많이 재생된 장르
    # 장르 내에서 많이 재생된 노래
    # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래
    
    answer = []
    temp = []
    total_genre_d = {}

    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))

    for g in temp:
        if g[0] not in total_genre_d:
            total_genre_d[g[0]] = g[1]
        else:
            total_genre_d[g[0]] += g[1]
    
    total_genre_d = sorted(total_genre_d.items(), key = lambda x: -x[1])
    print(total_genre_d)
    
    for i in total_genre_d:
        count = 0
        for j in temp:
            if i[0] == j[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 1, 3, 0]