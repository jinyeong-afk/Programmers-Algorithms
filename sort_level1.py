def solution(array, commands):
    answer = []
    slices = []
    for i,j,k in commands:
        slices = array[(i-1):(j)]
        slices.sort()
        answer.append(slices[k-1])
    return answer
