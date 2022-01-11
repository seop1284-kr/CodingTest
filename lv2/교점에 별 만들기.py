# https://programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    
    answer = []
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            res = func(line[i], line[j])
            if res:
                answer.append(res)
    xs, ys = zip(*answer)
    
    xmax = int(max(xs))
    ymax = int(max(ys))
    xmin = int(min(xs))
    ymin = int(min(ys))
    
    ans = []
    for y in range(ymax - ymin + 1):
        ans.append(['.'] * (xmax - xmin + 1))
    
    for x, y in zip(xs, ys):
        ans[int(y) - ymin][int(x) - xmin] = '*'
        print(x, y)
    
    for i in range(len(ans)):
        ans[i] = ''.join(ans[i])
    
    ans.reverse()
    return ans

def func(a, b):
    if a[0] * b[1] - a[1] * b[0]:
        x = (a[1] * b[2] - a[2] * b[1]) / (a[0] * b[1] - a[1] * b[0])
        y = (a[2] * b[0] - a[0] * b[2]) / (a[0] * b[1] - a[1] * b[0])
        if isInt(x) and isInt(y):
            return x, y
        
    return None
    
def isInt(x):
    if int(x) == x:
        return True
    else:
        return False
