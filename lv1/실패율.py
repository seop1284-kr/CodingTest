# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    people_num = len(stages)
    lst = []
    for i in range(1, N + 1):
        if people_num == 0:
            lst.append((i, 0))
            continue
        lst.append((i, stages.count(i) / people_num))
        people_num -= stages.count(i)
    lst.sort(reverse = True, key = lambda element : element[1])
    
    for t in lst:
        answer.append(t[0])
    return answer
