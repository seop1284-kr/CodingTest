# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    
    for n in range(1, len(land)):
        for i in range(4):
            land[n][i] += max(land[n - 1][:i] + land[n - 1][i + 1:])
    
    return max(land[-1])
