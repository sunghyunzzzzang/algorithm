# 16948. 데스나이트

from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(r1, c1, r2, c2):
    maps[r1][c1] = 1
    q.append((r1, c1))

    while q:
        x, y = q.popleft()
        # 목표 좌표 도착
        if x == r2 and y == c2:
            return maps[x][y] - 1
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if not nx in range(N) or not ny in range(N):
                continue
            # 방문 체크
            if maps[nx][ny] != 0:
                continue
            maps[nx][ny] = maps[x][y] + 1
            q.append((nx, ny))

    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
maps = [[0] * N for i in range(N)]

q = deque()

print(bfs(r1, c1, r2, c2))