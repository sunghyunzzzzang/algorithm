# 14442. 벽 부수고 이동하기 2
# dx, dy를 '상 하 좌 우'로 실행 시 시간초과

from collections import deque

# '상 우 하 좌'
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while q:
        x, y, k = q.popleft()

        # 도착
        if x == N - 1 and y == M - 1:
            return visited[x][y][k]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not nx in range(N) or not ny in range(M):
                continue
            if visited[nx][ny][k] != 0:
                continue
            # 벽 없을 때
            if maps[nx][ny] == 0:
                q.append((nx, ny, k))
                visited[nx][ny][k] = visited[x][y][k] + 1
            # 벽 있을 때 and 벽 부술 수 있는 횟수 체크
            elif maps[nx][ny] == 1 and k != K:
                q.append((nx, ny, k+1))
                visited[nx][ny][k+1] = visited[x][y][k] + 1

    return -1

# N: 세로 크기, M: 가로 크기, K: 벽 부술 수 있는 횟수
N, M, K = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, list(input()))))

visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1

result = bfs()
print(result)