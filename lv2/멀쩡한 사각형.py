# https://programmers.co.kr/learn/courses/30/lessons/62048
def solution(w,h):
    answer = w * h - (w + h - gcd(w, h))
    return answer

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
