# 2206. 벽 부수고 이동하기

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, q):

    q.append((x, y, 1))
    distance[x][y][1] = 1
    while q:
        x, y, skill = q.popleft()
        # 도착 했을 때
        if x == N - 1 and y == M - 1:
            return distance[x][y][skill]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if distance[nx][ny][skill] != 0:
                continue
            # 벽이 없을 때
            if maps[nx][ny] == 0:
                distance[nx][ny][skill] = distance[x][y][skill] + 1
                q.append((nx, ny, skill))
            # 벽이 있을 때 부술 수 있으면,
            elif maps[nx][ny] == 1 and skill == 1:
                distance[nx][ny][0] = distance[x][y][skill] + 1
                q.append((nx, ny, 0))

    return -1


N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, list(input()))))

distance = [[[0, 0] for j in range(M)] for i in range(N)]
q = deque()

result = bfs(0, 0, q)

print(result)