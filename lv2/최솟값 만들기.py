# https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    for x, y in zip(A, B):
        answer += x * y


    return answer
