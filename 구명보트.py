# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    escape = []
    for i in range(len(people)):
        if i in escape:
            continue
        for j in range(i + 1, len(people)):
            if j in escape:
                continue
            if people[i] + people[j] <= limit:
                escape.append(i)
                escape.append(j)
                print(i, j)
                answer += 1
                break
        else:
            escape.append(i)
            print(i)
            answer += 1
            
    return answer
