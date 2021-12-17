# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    
    return  max(price * (((count + 1) * count) / 2) - money, 0)
