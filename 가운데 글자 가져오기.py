# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    answer = ''
    c = len(s) // 2
    answer = s[c - 1:c + 1] if len(s) % 2 == 0 else s[c]
    return answer
