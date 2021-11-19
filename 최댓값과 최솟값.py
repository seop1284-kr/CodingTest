# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    i = [int(n) for n in s.split()]
    answer = ' '.join([str(min(i)), str(max(i))])
    return answer
