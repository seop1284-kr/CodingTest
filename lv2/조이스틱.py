# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    s = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    
    idx = 0
    l = len(name)
    
    print(s[-1])
    while True:
        
        answer += s[idx]
        s[idx] = 0
        
        if sum(s) == 0: break
        
        left, right = 1, 1
        while s[idx - left] == 0:
            left += 1
        while s[idx + right] == 0:  
            right += 1
        
        answer += min(left, right)
        idx += -left if left < right else right
    
    
    return answer
