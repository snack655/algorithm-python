from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(answer)
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))