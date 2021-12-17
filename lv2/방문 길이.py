# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    answer = 0
    xvisited = [[0 for col in range(10)] for row in range(11)]
    yvisited = [[0 for col in range(11)] for row in range(10)]
     
    x, y = 5, 5
     
    for v in dirs:
        if v == 'L' and x > 0:
            x -= 1
            xvisited[y][x] = 1
            print(v, x, y)
        elif v == 'R' and x < 10:
            xvisited[y][x] = 1
            x += 1
            print(v, x, y)

        elif v == 'U' and y < 10:
            yvisited[y][x] = 1
            y += 1
            print(v, x, y)
        elif v == 'D' and y > 0:
            y -= 1
            yvisited[y][x] = 1
            print(v, x, y)
            
    for r in xvisited:
        answer += sum(r)
    for r in yvisited:
        answer += sum(r)
    return answer
