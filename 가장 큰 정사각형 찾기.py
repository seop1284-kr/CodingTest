# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 1234
    
    for i in range(len(board)):
        board[i].append(0)
    board.append([0 for i in range(len(board[0]))])
    
    xlen = len(board)
    ylen = len(board[0])
    
    max = 0
    
    for x in range(xlen):
        for y in range(ylen):
            if board[x][y] == 1:
                tempx = x
                tempy = y
                l = 0
                while True:
                    if board[tempx][tempy] == 1:
                        l += 1
                    else:
                        break
                    tempy += 1
                flag = True
                for i in range(l):
                    if (sum(board[tempx + i][y: y + l]) != l):
                        flag = False
                        break
                if flag:
                    if max < l * l:
                        max = l * l
                
                    
    
    answer = max
    
    return answer
