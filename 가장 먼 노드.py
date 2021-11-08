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

# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
# 인접 행렬 사용하여 시간 초과 해결
import copy

def solution(n, edge):
    
    # 인접 행렬 만듬
    adjs = [[] for row in range(n + 1)]
    for v in edge:
        adjs[v[0]].append(v[1])
        adjs[v[1]].append(v[0])
        
    # 방문 노드
    visited = [False for i in range(n + 1)]
    visited[1] = True
    
    queue = [1]
    temp = []

    while queue:
        temp = copy.deepcopy(queue)
        for n in temp:
            queue.pop(0)
            for tnode in adjs[n]:
                if visited[tnode]:
                    continue
                visited[tnode] = True
                queue.append(tnode)
    
    return len(temp)
