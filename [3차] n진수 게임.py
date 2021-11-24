# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    
    # p의 순서 인덱스 배열
    porder = [i * m + p for i in range(t)]
    
    # 가장 높은 p의 순서 인덱스
    pmax = max(porder)
    
    # 시작 숫자
    number = 1
    s = '0'
    
    # pmax를 얻을 수 있을 때 까지 n진수 문자열 나열함 
    while pmax >= len(s):
        s += to_n_number(number, n)
        number += 1
    
    # 결과 가져오기
    for i in porder:
        answer += s[i - 1]
    
    return answer

# n진수 문자열 구하기
def to_n_number(number, n):
    nc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    temp = ''
    while number:
        na = number % n
        number //= n
        temp = nc[na] + temp
    return temp
