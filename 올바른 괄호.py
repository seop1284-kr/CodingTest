# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    stack = []
    for v in s:
        if v == ')':
            if not stack or stack.pop() != '(':
                return False
        else:
            stack.append(v)
    if stack:
        return False
    
    return True
