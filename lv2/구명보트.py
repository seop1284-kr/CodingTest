# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 1
    while answer + i <= len(people):
        if people[answer] + people[-i] <= limit:
            i += 1
        answer += 1
    return answer
