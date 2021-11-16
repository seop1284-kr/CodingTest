# https://programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    xlen = len(arr1)
    ylen = len(arr2[0])
    answer = [[0 for col in range(ylen)] for row in range(xlen)]

    x = 0
    
    for a1 in arr1:
        y = 0
        temp = 0
        for a2 in zip(*arr2):
            for i in range(len(arr1[0])):
                answer[x][y] += a1[i] * a2[i]
            y += 1
        x += 1
                    
        
    return answer
