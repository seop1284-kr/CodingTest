# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

# 방문한 노드
visited = []

# 정답
answer = 0

def solution(n, computers):
    global answer
    global visited
    
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            bfs(n, computers, i)
            
    return answer

def bfs(n, computers, cur):
    global answer
    global visited
    
    # bfs를 위한 스택
    stack = []
    stack.append(cur)
    
    # 방문 노드 1
    visited[cur] = 1
    
    # 현재 노드로 부터 bfs로 모든 곳 방문 했을 때
    while len(stack) != 0:
        for i in range(n):
            if computers[cur][i] == 1 and visited[i] == 0:
                visited[i] = 1
                stack.append(i)
        cur = stack.pop()

    answer += 1
