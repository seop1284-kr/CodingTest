# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = n
    
    # 정렬
    lost.sort()
    reserve.sort()
    
    # 잃어버린 사람 (자기자신, 앞사람, 뒷사람 순으로) 여분 체크
    # 여분 있으면 빌리고 없앰
    for v in lost:
        if v in reserve:
            reserve.remove(v)
        elif v - 1 in reserve and v - 1 not in lost:
            reserve.remove(v - 1)
        elif v + 1 in reserve and v + 1 not in lost:
            reserve.remove(v + 1)
        else:
            answer -= 1
    return answer
