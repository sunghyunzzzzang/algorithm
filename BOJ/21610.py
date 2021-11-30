# 21610. 마법사 상어와 비바라기

from collections import deque

# 구름의 이동 방향
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 물 복사 버그의 방향
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, -1, 1]

# N: 배열 크기, M: 구름의 이동 정보
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

command = deque()
for i in range(M):
    command.append(list(map(int, input().split())))

# 시작 지점 저장
start = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]
cloud = deque(start)

copy_water = deque()

while command:
    dir, dist = command.popleft()

    # 동작 1, 2, 3
    for i in range(len(cloud)):
        # 모든 구름이 이동 (동작 1)
        x, y = cloud.popleft()
        nx = ((x + (dx[dir] * dist)) + N) % N
        ny = ((y + (dy[dir] * dist)) + N) % N
        # 구름이 있는 칸의 물의 양이 1 증가, 구름 사라짐 (동작 2, 3)
        maps[nx][ny] += 1
        # 물복사버그 마법 사용할 좌표 저장
        copy_water.append((nx, ny))

    visited = [[0] * N for i in range(N)]
    # 동작 4
    for i in range(len(copy_water)):
        x, y = copy_water.popleft()
        for d in range(4):
            nnx = x + ddx[d]
            nny = y + ddy[d]
            # 배열 범위 체크
            if nnx not in range(N) or nny not in range(N):
                continue
            # 물이 있으면
            if maps[nnx][nny] >= 1:
                maps[x][y] += 1
        # 구름이 방금 없어진 곳 체크
        visited[x][y] = 1

    # 동작 5
    for i in range(N):
        for j in range(N):
            # 구름이 방금 없어진 곳이면
            if visited[i][j] == 1:
                continue
            # 물의 양이 2 이상인 곳
            if maps[i][j] >= 2:
                maps[i][j] -= 2
                cloud.append((i, j))

# 물의 양의 합 출력
print(sum(map(sum, maps)))