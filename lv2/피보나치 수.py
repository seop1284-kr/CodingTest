# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])
    
    answer = (lst[n - 2] + lst[n - 1]) % 1234567
    
    return answer
