# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 1 and x != 0 and y != 0:
                board[x][y] = min([board[x - 1][y - 1], board[x][y - 1], board[x - 1][y]]) + 1
    
    answer = 0          
    for row in board:
        if answer < max(row):
            answer = max(row)
    
    return answer * answer
