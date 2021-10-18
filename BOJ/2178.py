# 2178. 미로탐색

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global result
    q = deque()
    q.append((x, y))
    distance[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if distance[nx][ny] != 0:
                continue
            # 이동할 수 없는 칸 체크
            if maps[nx][ny] == 0:
                continue

            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))

            # 도착 했을 때
            if nx == N-1 and ny == M-1:
                result = distance[nx][ny]
                return

# N: 세로크기 , M: 가로크기
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, list(input()))))

distance = [[0] * M for i in range(N)]
result = 0

dfs(0, 0)

print(result)