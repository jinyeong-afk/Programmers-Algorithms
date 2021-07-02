import math
def solution(answers):
    answer = []
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    answer1Count=0
    answer2Count=0
    answer3Count=0
    answer1 = answer1 * math.ceil(len(answers) / len(answer1))
    answer2 = answer2 * math.ceil(len(answers) / len(answer2))
    answer3 = answer3 * math.ceil(len(answers) / len(answer3))
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            answer1Count += 1
        if answers[i] == answer2[i]:
            answer2Count += 1
        if answers[i] == answer3[i]:
            answer3Count += 1
    maxNum = answer1Count
    answer = [1]
    if maxNum < answer2Count:
        maxNum = answer2Count
        answer = [2]
    elif maxNum == answer2Count:
        answer.append(2)
    if maxNum < answer3Count:
        answer = [3]
    elif maxNum == answer3Count:
        answer.append(3)
    return answer

#-------------------------------------------------
#또 다른 풀이

def solution(answers):
    answer = []
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for idx, ans in enumerate(answers):
        if ans == answer1[idx%len(answer1)]:
            score[0] += 1
        if ans == answer2[idx%len(answer2)]:
            score[1] += 1
        if ans == answer3[idx%len(answer3)]:
            score[2] += 1
            
    for idx2, sco in enumerate(score):
        if sco == max(score):
            answer.append(idx2+1)
    return answer
