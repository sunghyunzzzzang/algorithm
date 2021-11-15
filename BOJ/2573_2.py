# 2573. 빙산
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx not in range(N) or ny not in range(M):
                continue

            if visited[nx][ny] != 0:
                 continue

            if maps[nx][ny] > 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))


days = 0
while 1:
    # 빙산이 다 녹으면 break
    if max(map(max, maps)) <= 0:
        break

    temp = [[0] * M for i in range(N)]
    visited = [[0] * M for i in range(N)]
    cnt = 0

    days += 1

    # 빙산 주변 값이 바닷물이면 temp에 값 넣어줌
    for i in range(N):
        for j in range(M):
            # 빙산
            if maps[i][j] > 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx not in range(N) or ny not in range(M):
                        continue
                    # 주변 값이 0보다 작으면
                    if maps[nx][ny] <= 0:
                        temp[i][j] += 1

    # 빙산 높이 계산
    for i in range(N):
        for j in range(M):
            if maps[i][j] > 0:
                maps[i][j] = maps[i][j] - temp[i][j]

    # 빙산 개수
    for i in range(N):
        for j in range(M):
            if maps[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j, visited)
                cnt += 1

    # 빙산 개수가 2개 이상이면
    if cnt >= 2:
        break

# 빙산이 다 녹을 때까지 분리되지 않으면 0 출력
if max(map(max, maps)) <= 0:
    days = 0

print(days)