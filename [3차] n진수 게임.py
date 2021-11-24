# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    cnt = 1
    number = 1
    q = '0'
    
    while t:
        if len(q) < cnt:
            q += to_n_number(number, n)
            number += 1
        
        num = q[cnt - 1]
        if cnt % m == p:
            answer += num
            t -= 1
            
        cnt += 1

    return answer

def to_n_number(number, n):
    nc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    temp = ''
    while number:
        na = number % n
        number //= n
        temp = nc[na] + temp
    return temp
