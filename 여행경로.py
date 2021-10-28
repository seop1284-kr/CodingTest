# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

# 방문한 노드 
visited = []
# 정답 리스트
answer = []

def solution(tickets):
    global visited
    global answer
    
    visited = [0 for i in range(len(tickets))]
    answer = []
    
    dfs('ICN', tickets, ['ICN'])
    
    return answer

def dfs(start, tickets, stack):
    global answer
    
    # 정답에 도달
    if len(stack) == len(tickets) + 1:
        for v in stack:
            answer.append(v)
        # 정답 도달하면 True 반환
        return True
    
    # 가능 티켓 리스트
    tmp = []
    
    # 가능 티켓 리스트 추가
    for i in range(len(tickets)):
        if start == tickets[i][0] and visited[i] == 0:
            tmp.append((i, tickets[i][1]))
    
    # 가능 티켓 리스트 정렬
    tmp = sorted(tmp, key=lambda x: x[1])
    
    # 가능 티켓 리스트의 첫번째 요소로 이동
    for i in range(len(tmp)):
        # 방문한 노드로 변경
        visited[tmp[i][0]] = 1 
        # 정답 스택에 추가
        stack.append(tmp[i][1])
        
        # 방문, 정답에 도달하면 True 리턴
        if dfs(tmp[i][1], tickets, stack):
            return True
        
        # 방문한 노드 해제
        visited[tmp[i][0]] = 0
        # 정답 스택에서 빼기
        stack.pop()
