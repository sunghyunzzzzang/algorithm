# 15657. N과 M(8)

def run(lev, start):
    global M
    if lev == M:
        print(*arr)
        return
    for i in range(start, len(Num)):
        arr.append(Num[i])
        run(lev+1, i)
        arr.pop()

N, M = map(int, input().split())
Num = list(map(int, input().split()))
Num.sort()
arr = []
run(0, 0)