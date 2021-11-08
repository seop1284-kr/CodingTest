# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
# 시간초과!

def solution(n, edge):
    answer = 0
    visited = [1]
    queue = [1]
    while queue:
        temp = []
        for n in queue:
            for v in edge:
                if v[0] == n and v[1] not in visited:
                    temp.append(v[1])
                    visited.append(v[1])
                elif v[1] == n and v[0] not in visited:
                    temp.append(v[0])
                    visited.append(v[0])

        
        if not temp:
            answer = len(queue)
            break 
        
        queue = temp
                
    return answer
