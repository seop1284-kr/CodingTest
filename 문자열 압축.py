# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = 0
    ans = ''
    if len(s) == 1:
        return 1
    
    # 문자열 자르는 단위를 1 부터 문자열 길이 까지 for 문
    for n in range(1, len(s)):
        ans = ''
        cnt = 1
        temp = s[:n]
        # 마지막 검사를 위해 len(s) + 1 까지 체크한다.
        for l in range(1, len(s) + 1):
            
            if temp == s[n * l : n + n * l]:
                cnt += 1
            else:
                ans += temp
                if cnt != 1:
                    ans += str(cnt)
                cnt = 1
                temp = s[n * l : n + n * l]

        # 결과 길이를 재서 최소 값을 저장
        if answer == 0 or answer > len(ans):
            answer = len(ans)
        
    
    return answer
