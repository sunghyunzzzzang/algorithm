# 15652. N과 M (4)

def run(lev, start):
    if lev == M:
        print(*arr)
        return
    for i in range(start, N+1):
        arr.append(i)
        run(lev+1, i)
        arr.pop()

N, M = map(int, input().split())
arr = []
run(0, 1)