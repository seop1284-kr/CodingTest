# https://programmers.co.kr/learn/courses/30/lessons/12913
max_sum = 0

def solution(land):
    answer = 0    
            
    dfs(0, -1, 0, len(land), land)
    print(len(land))
    return max_sum

def dfs(d, idx, s, l, land):
    global max_sum
    
    if d == l:
        if max_sum < s:
            max_sum = s
        return
    
    for i in range(4):
        
        if i is idx:
            continue
        
        dfs(d + 1, i, s + land[d][i], l, land)
