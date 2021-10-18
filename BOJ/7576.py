# 7576. 토마토

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                continue
            # 토마토가 들어있는 칸인지 체크
            if maps[nx][ny] == -1:
                continue

            maps[nx][ny] = maps[x][y] + 1
            visited[nx][ny] = 1
            q.append((nx, ny))




M, N = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

visited = [[0] * M for i in range(N)]
result = 0
q = deque()

# 토마토 위치 q에 저장
for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

bfs()

# 결과값
result = (max(map(max, maps))) - 1
# 토마토가 모두 익지 못하면 -1 출력
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            result = -1

print(result)
