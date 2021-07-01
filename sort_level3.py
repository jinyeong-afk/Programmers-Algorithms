def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[-1]+1):
        print(i)
        if i == sum(i <= x for x in citations):
            print(i, ", ", answer)
            answer = i
            return answer
        if i <= sum(i <= x for x in citations):
            answer = i        
    return answer
