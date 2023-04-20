import math

def solution(r1, r2):
    r1Num = getNumOfDots(r1) - 4
    r2Num = getNumOfDots(r2)  
    return r2Num - r1Num

def getNumOfDots(r):
    rNum = 0
    for i in range(1, r):
        rNum += getMaxY(r, i)
    rNum *= 4
    rNum += (4*r) + 1
    return rNum

def getMaxY(r, x):
    y = math.sqrt(r**2 - x**2)
    return int(y)

#print(getMaxY(5, 1))
print(solution(2, 3))