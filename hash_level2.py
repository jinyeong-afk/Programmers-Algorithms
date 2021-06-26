# 첫번째 테스트: 효율성 테스트 실패

def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(len(phone_book)-i-1):
            if phone_book[j+i+1].find(phone_book[i]) == 0:
                answer = False
                return answer
    return answer

#두번째 테스트
#배운점: 숫자로 된 문자열은 정렬하면 숫자 크기순이 아닌 사전순으로 정렬이 된다.

def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
            answer = False
            return answer
    return answer
