# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, i, val):
    res = 0
    if i == len(numbers):
        if target == val:
            return 1
        else:
            return 0
    
    res += dfs(numbers, target, i + 1, val + numbers[i])
    res += dfs(numbers, target, i + 1, val - numbers[i])
    
    return res
