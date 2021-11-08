# 11724. 연결 요소의 개수

from collections import deque

def bfs(s):
    global result
    q = deque()
    q.append(s)
    visited[s] = 1
    result += 1
    while q:
        x = q.popleft()
        for d in range(len(maps[x])):
            nx = maps[x][d]
            if visited[nx] != 0:
                continue
            visited[nx] = 1
            q.append(nx)


N, M = map(int, input().split())
maps = [[] * (N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

visited = [0] * (N+1)
result = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)

print(result)