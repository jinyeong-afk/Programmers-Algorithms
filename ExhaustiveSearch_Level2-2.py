import math
def solution(brown, yellow):
    result = []
    for i in range(1,yellow+1):
        if yellow % i == 0:
            result.append(i)
    for j in range(len(result)//2+1):
        if (result[j]+2) * (result[-j-1]+2) - yellow == brown:
            return [result[-j-1]+2,result[j]+2]
