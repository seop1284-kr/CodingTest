# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = 0
    ans = ''

    for n in range(1, len(s)):
        cnt = 1
        temp = s[:n]
        print(len(s) // n)
        for l in range(1, len(s) // n):
            if temp == s[n * l : n + n * l]:
                cnt += 1
            else:
                ans += temp
                if cnt != 1:
                    ans += str(cnt)
                cnt = 1
                temp = s[n * l : n + n * l]
            
            # 마지막
            if l == len(s) - 1:
                ans += temp
                if cnt != 1:
                    ans += str(cnt)
                cnt = 1
                
        
        print(ans)
        if answer == 0 or answer > len(ans):
            answer = len(ans)
        ans = ''
    
    return answer
