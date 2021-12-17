# https://programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    answer = 0
    m = max(arr)

    while True:
        flag = True
        for v in arr:
            if m % v != 0:
                flag = False
        if flag:
            break
        m += 1
    return m
