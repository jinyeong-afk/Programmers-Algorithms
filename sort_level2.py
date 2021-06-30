def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    numbers = str(int(''.join(numbers)))
    answer = numbers
    return answer
