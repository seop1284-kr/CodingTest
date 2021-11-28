# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    answer = 0
    xvisited = [[0 for col in range(11)] for row in range(10)]
    yvisited = [[0 for col in range(10)] for row in range(11)]
     
    x, y = 5, 5
    xfirst, yfirst = True, True
     
    for i in range(len(dirs)):
        v = dirs[i]
        if v == 'L' and x > 0:
            if xfirst:
                x1 = 5
                xfirst = False
            x -= 1
            x1 -= 1
            xvisited[y][x1] = 1

        elif v == 'R' and x < 10:
            if xfirst:
                x1 = 4
                xfirst = False
            x += 1
            x1 += 1
            xvisited[y][x1] = 1

        elif v == 'U' and y < 10:
            if yfirst:
                y1 = 4
                yfirst = False
            y += 1
            y1 += 1
            yvisited[y1][x] = 1

        elif v == 'D' and y > 0:
            if yfirst:
                y1 = 5
                yfirst = False
            y -= 1
            y1 -= 1
            yvisited[y1][x] = 1


    
    for row in zip(*xvisited, *yvisited):
        answer += sum(row)
    return answer
