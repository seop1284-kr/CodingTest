# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3#

def solution(n):
    answer = ''
    
    
    while n:
        # 몫, 나머지
        q, r = divmod(n, 3)
        
        # 0이 없어서..
        if r == 0:
            n -= 1  
            r = 3
        
        n = n // 3
        
        answer = str(r) + answer
        
    answer = answer.replace('3', '4')
    

    return answer
