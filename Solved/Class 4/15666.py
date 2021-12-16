# 15666. N과 M(12)

import copy

def run(lev, start):
    global M
    if lev == M:
        if arr not in dict:
            print(*arr)
            temp = copy.deepcopy(arr)
            dict.append(temp)
        return
    for i in range(start, len(Num)):
        arr.append(Num[i])
        run(lev+1, i)
        arr.pop()


N, M = map(int, input().split())
Num = list(map(int, input().split()))
Num.sort()
arr = []
used = [0] * N
dict = []
run(0, 0)