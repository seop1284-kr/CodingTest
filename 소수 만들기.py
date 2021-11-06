# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
# 시간초과!
answer = 0

def solution(nums):
    arr = list(i for i in range(len(nums)))
    comb(arr, nums, 0, 3, 0, 0)
    return answer

def comb(arr, nums, depth, r, index, target):
    global answer

    if depth == r and check(arr, nums, r):
        answer += 1
        return
    elif target == len(arr):
        return
    else:
        arr[index] = target
        comb(arr, nums, depth + 1, r, index + 1, target + 1)
        comb(arr, nums, depth, r, index, target + 1)
    
    
def check(arr, nums, r):
    sum = 0
    for i in range(3):
        sum += nums[arr[i]]
    
    for i in range(2, sum - 1):
        if sum % i == 0:
            return False
    
    return True
