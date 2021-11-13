# 7569. 토마토

from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global result
    while q:
        x, y, z, cnt = q.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            # 배열 범위 체크
            if nx not in range(N) or ny not in range(M) or nz not in range(H):
                continue
            # 익지 않은 토마토 일 때
            if maps[nz][nx][ny] == 0:
                maps[nz][nx][ny] = maps[z][x][y] + 1
                q.append((nx, ny, nz, cnt+1))
                result = cnt + 1

def check():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if maps[h][i][j] == 0:
                    return 0

    return 1

M, N, H = map(int, input().split())
result = 0
maps = [[] for i in range(H)]
for h in range(H):
    for i in range(N):
        maps[h].append(list(map(int, input().split())))

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            # 익은 토마토 일 떄
            if maps[h][i][j] == 1:
                q.append((i, j, h, 0))
bfs()

# 모두 익었으면
if check():
    print(result)
# 익지 않은 토마토가 있으면
else:
    print(-1)