# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    # 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    answer = ''
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = week[(sum(day[:a - 1]) + b ) % 7]
    return answer
