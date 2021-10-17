# 10966. 물놀이를 가자

from collections import deque


# 상 하 좌 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():
    while q:
        x, y = q.popleft()


        for dx ,dy in d:
            nx = x + dx
            ny = y + dy
            if not nx in range(N) or not ny in range(M):
                continue

            if visited[nx][ny] != -1: continue
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))



TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    maps = []
    for i in range(N):
        maps.append(list(input()))

    visited = [[-1] * M for i in range(N)]
    distance = [[0] * M for i in range(N)]
    answer = 0
    q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    bfs()
    for i in range(N):
        for j in range(M):
            answer += visited[i][j]
    print("#{} {}".format(tc, answer))