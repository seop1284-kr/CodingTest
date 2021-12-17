# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    test = [1 if v is True else -1 for v in signs]
    
    for i in range(len(absolutes)):
        answer += absolutes[i] * test[i]
        
    return answer
