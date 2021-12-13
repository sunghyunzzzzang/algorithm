# 15654. N과 M(5)

def run(lev):
    global M
    if lev == M:
        print(*arr)
        return
    for i in range(len(Num)):
        if used[i] == 0:
            used[i] = 1
            arr.append(Num[i])
            run(lev+1)
            arr.pop()
            used[i] = 0

N, M = map(int, input().split())
Num = list(map(int, input().split()))
Num.sort()
arr = []
used = [0] * N
run(0)