# 16236. 아기 상어

from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs():
    global size, feed, move, s_x, s_y
    q = deque()
    q.append((s_x, s_y))
    visited = [[0] * N for i in range(N)]
    visited[s_x][s_y] = 1
    eat = []
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if nx not in range(N) or ny not in range(N):
                continue
            # 방문 체크
            if visited[nx][ny] != 0:
                continue
            # 아기 상어보다 물고기가 크면
            if size < maps[nx][ny]:
                continue
            # 먹을 수 있는 물고기가 있으면
            elif size > maps[nx][ny] and maps[nx][ny] != 0:
                eat.append((nx, ny, visited[x][y]))
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

    # 먹을 수 있는 물고기가 없으면
    if not eat:
        return -1, -1, -1

    # 거리가 가깝고 행과 열 값이 가장 작은 물고기 부터 먹는다
    eat.sort(key = lambda x: (x[2],x[0], x[1]))
    return eat[0][0], eat[0][1], eat[0][2]

def check():
    global s_x, s_y
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 9:
                s_x = i
                s_y = j

N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

size = 2
feed = 0
result = 0
s_x = 0
s_y = 0

# 상어 위치
check()

while 1:
    x, y, move = bfs()
    # 먹을 수 있는 물고기가 없으면
    if x == -1:
        break

    # maps에 아기 상어 위치 저장
    maps[s_x][s_y] = 0
    maps[x][y] = 9

    # 먹은 횟수 증가
    feed += 1
    # 아기상어 크기만큼 먹었으면 크기 증가
    if size == feed:
        size += 1
        feed = 0

    # 아기 상어 시작 위치 저장
    s_x = x
    s_y = y

    # 시간 저장
    result += move

print(result)