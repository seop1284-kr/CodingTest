# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    flag = True
    for c in s:
        if flag:
            c = c.upper()
            flag = False
        else:
            c = c.lower()
            
        if c == ' ':
            flag = True
        
        answer += c
    return answer
