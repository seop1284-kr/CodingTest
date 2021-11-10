# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    answer = len(nums) // 2
    poket_set = {p for p in nums}
    print(poket_set)
    if len(poket_set) < answer:
        return len(poket_set)
    return answer
