# 10026. 적록색약

from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs1(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    visited1[s_x][s_y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if not nx in range(N) or not ny in range(N):
                continue
            # 방문 체크
            if visited1[nx][ny] != 0:
                continue
            # 같은 색인지 체크
            if maps[nx][ny] != maps[s_x][s_y]:
                continue
            q.append((nx, ny))
            visited1[nx][ny] = 1


def bfs2(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    visited1[s_x][s_y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if not nx in range(N) or not ny in range(N):
                continue
            # 방문 체크
            if visited2[nx][ny] != 0:
                continue

            # 시작 색이 'B'일 때
            if maps[s_x][s_y] == 'B':
                # 다른 칸 색이 'R'와 'G'면
                if maps[s_x][s_y] != maps[nx][ny]:
                    continue
            # 시작 색이 'R'와 'G'일 떄
            else:
                # 다른 칸 색이 'B'면
                if maps[nx][ny] == 'B':
                    continue

            q.append((nx, ny))
            visited2[nx][ny] = 1

# N : 배열 크기
N = int(input())
maps = []
for i in range(N):
    maps.append(list(input()))

visited1 = [[0] * N for i in range(N)]
result1 = 0

visited2 = [[0] * N for i in range(N)]
result2 = 0

for i in range(N):
    for j in range(N):
        # 정상
        if visited1[i][j] == 0:
            bfs1(i, j)
            result1 += 1
        # 적록색약
        if visited2[i][j] == 0:
            bfs2(i, j)
            result2 += 1

print(result1, result2)