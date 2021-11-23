# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
def solution(n):
    answer = count_one(n)
    
    while True:
        n = n + 1
        if count_one(n) == answer:
            return n

def count_one(number):
    res = 0
    while number:
        na = number % 2
        number //= 2
        if (na == 1): res += 1
    
    return res
