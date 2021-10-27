# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# 방문한 노드
visited = []

# 정답 전역 변수로
answer = 0

def solution(begin, target, words):
    global visited
    
    # 방문한 노드 초기화
    visited = [0 for i in range(len(words))]
    
    # dfs 실행
    dfs(begin, target, words, 0)
    
    return answer

def dfs(begin, target, words, cnt):
    global visited
    global answer
    
    # 타겟에 도착한 경우
    if begin == target:
        if answer == 0 or answer > cnt:
            answer = cnt
    
    
    for idx, word in enumerate(words):
        # 이동 가능 and 방문 안한 노드
        if check(begin, word) and visited[idx] == 0:
            # 방문으로 변경, 방문, 방문안함으로 변경
            visited[idx] = 1          
            dfs(word, target, words, cnt + 1)
            visited[idx] = 0
        
# 이동 가능 체크 함수        
def check(a, b):
    cnt = 0
    for i in range(len(b)):
        if b[i] != a[i]:
            cnt += 1
    
    if cnt == 1:
        return True
    return False
