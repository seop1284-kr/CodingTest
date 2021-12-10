# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = s.count('1')
        s = str(format(s, 'b'))

    return answer
