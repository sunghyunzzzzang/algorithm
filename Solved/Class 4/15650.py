# 15650 N과 M (2)

def run(lev, start):
    if lev == M:
        print(*arr)
        return
    for i in range(start, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            run(lev+1, i)
            arr.pop()
            visited[i] = 0

N, M = map(int, input().split())
arr = []
visited = [0] * (N+1)
run(0, 1)