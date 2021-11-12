# https://programmers.co.kr/learn/courses/30/lessons/42883
# 시간 초과!
def solution(number, k):
    answer = ''
    n = len(number) - k
    while n:
        max = 0
        idx = 0
        for i in range(len(number) - n + 1):
            if max < int(number[i]):
                max = int(number[i])
                idx = i
        
        n -= 1
        answer += number[idx]
        number = number[idx + 1:]
    
    
    return answer
