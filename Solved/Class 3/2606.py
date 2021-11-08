# 2606. 바이러스

from collections import deque

def bfs():
    q = deque()
    q.append(1)
    visited = [0] * (N+1)
    visited[1] = 1
    result = 0
    while q:
        x = q.popleft()
        for i in range(len(maps[x])):
            nx = maps[x][i]
            if visited[nx] == 1:
                continue
            visited[nx] = 1
            q.append(nx)
            result += 1

    return result

N = int(input())
V = int(input())
maps = [[] * (N+1) for i in range(N+1)]

for i in range(V):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

print(bfs())