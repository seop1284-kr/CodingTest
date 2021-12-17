# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    queue = []
    
    for m in moves:
        for b in board:
            if b[m-1] == 0:
                continue
            else:
                queue.append(b[m-1])
                b[m-1] = 0
                break
                
        if len(queue) > 1:
            if queue[-1] == queue[-2]:
                answer += 2
                queue.pop()
                queue.pop()
    
    return answer
