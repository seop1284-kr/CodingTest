# https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for x in range(len(numbers) - 1):
        for y in range(x + 1, len(numbers)):
            answer.append(numbers[x] + numbers[y])
    return sorted(list(set(answer)))
