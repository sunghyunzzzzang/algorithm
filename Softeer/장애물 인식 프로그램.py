# 장애물 인식 프로그램

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    check[s_x][s_y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx not in range(N) or ny not in range(N):
                continue
            if maps[nx][ny] == 0:
                continue
            if check[nx][ny] != 0:
                continue
            check[nx][ny] = 1
            q.append((nx, ny))
            cnt += 1
    return cnt

N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input())))

check = [[0] * N for i in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if check[i][j] == 0:
            if maps[i][j] == 1:
                result = bfs(i, j)
                answer.append(result)

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])