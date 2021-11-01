# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    answer = []
    
    # uid : 이름 딕셔너리
    names = {}
    
    # uid : 이름 딕셔너리 채우기
    for v in record:
        v = v.split()
        if v[0] == 'Change':
            names[v[1]] = v[2]
        elif v[0] == 'Enter':
            names[v[1]] = v[2]
    
    # 결과 채우기
    for v in record:
        v = v.split()
        if v[0] == 'Enter':
            answer.append(names[v[1]] + "님이 들어왔습니다.")
        elif v[0] == 'Leave':
            answer.append(names[v[1]] + "님이 나갔습니다.")
            
            
    return answer
