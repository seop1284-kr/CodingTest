# https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    answer = sum([i if n % i == 0 else 0 for i in range(1, n + 1)])
    return answer
