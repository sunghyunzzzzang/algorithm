# 1932. 정수 삼각형
# BFS

from collections import deque

dx = [1, 1]
dy = [0, 1]

def bfs(distance):

    while q:
        x, y, level = q.popleft()
        if level == N:
            continue
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]

            temp = distance[x][y] + maps[nx][ny]
            if distance[nx][ny] < temp:
                distance[nx][ny] = temp
                q.append((nx, ny, level+1))


N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

distance = [[0] * N for i in range(N)]
distance[0][0] = maps[0][0]
q = deque()
q.append((0, 0, 1))

bfs(distance)

print(max(distance[N-1]))