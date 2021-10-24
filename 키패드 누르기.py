# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    left = (0, 3)
    right = (2, 3)
    for v in numbers:
        if v == 1 or v == 4 or v == 7:
            answer += 'L'
            left = (0, v // 3)
        elif v == 3 or v == 6 or v == 9:
            answer += 'R'
            right = (2, (v // 3) - 1)
        else:
            pos = (1, 3) if v == 0 else (1, v // 3)
            lDist = abs(left[0] - pos[0]) + abs(left[1] - pos[1])
            rDist = abs(right[0] - pos[0]) + abs(right[1] - pos[1])
            if lDist > rDist:
                answer += 'R'
                right = (pos[0], pos[1])
            elif rDist > lDist:
                answer += 'L'
                left = (pos[0], pos[1])
            else:
                if hand == 'right':
                    answer += 'R'
                    right = (pos[0], pos[1])
                else:
                    answer += 'L'
                    left = (pos[0], pos[1])
        
        
    return answer
