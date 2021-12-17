# https://programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    answer = -1
    answer = sum(range(10)) - sum(numbers)
    
    return answer
