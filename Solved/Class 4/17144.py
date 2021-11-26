# 17144. 미세먼지 안녕!

import copy

# 시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def search():
    for i in range(N):
        for j in range(M):
            if maps[i][j] == -1:
                head = i
                body = i + 1
                return head, body

def run1():
    global maps
    temp = [[0] * M for i in range(N)]

    # temp에 공기청정기, 5보다 작은 미세먼지 값 저장
    for i in range(N):
        for j in range(M):
            if maps[i][j] < 5:
                temp[i][j] = maps[i][j]

    for i in range(N):
        for j in range(M):
            # 미세먼지 값이 5 이상이면 확산 가능
            if maps[i][j] >= 5:
                cnt = 4
                diffusion = maps[i][j] // 5
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 범위 체크
                    if nx not in range(N) or ny not in range(M):
                        cnt -= 1
                        continue
                    # 공기청정기 체크
                    if maps[nx][ny] == -1:
                        cnt -= 1
                        continue

                    # 확산되는 미세먼지 값
                    temp[nx][ny] += diffusion
                # 원래 칸 미세먼지 값
                temp[i][j] += maps[i][j] - (diffusion * cnt)

    maps = copy.deepcopy(temp)

def run2():
    # 공기청정기 위쪽 동작
    # 시계 방향
    dir = 0
    x, y = head - 1, 0

    while 1:
        # 경계값 체크
        if x == head and y == M - 1:
            dir = (dir + 1) % 4
        if x == 0 and y == M - 1:
            dir = (dir + 1) % 4
        if x == 0 and y == 0:
            dir = (dir + 1) % 4

        # 한 칸씩 이동
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 공기청정기 도착하면
        if maps[nx][ny] == -1:
            maps[x][y] = 0
            break

        # 다음 칸 값 저장
        maps[x][y] = maps[nx][ny]
        # 현재 위치 저장
        x = nx
        y = ny


    # 공기청정기 아래쪽 동작
    # 반시계 방향
    dir = 2
    x, y = body + 1, 0

    while 1:
        # 경계값 체크
        if x == body and y == M - 1:
            dir = (dir + 3) % 4
        if x == N - 1 and y == M - 1:
            dir = (dir + 3) % 4
        if x == N - 1 and y == 0:
            dir = (dir + 3) % 4

        # 한 칸씩 이동
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 공기청정기 도착하면
        if maps[nx][ny] == -1:
            maps[x][y] = 0
            break

        # 다음 칸 값 저장
        maps[x][y] = maps[nx][ny]
        # 현재 위치 저장
        x = nx
        y = ny


N, M, T = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

# 공기청정기 위치 찾기
head, body = search()

# 시뮬레이션
while T != 0:
    # 동작 1번
    run1()
    # 동작 2번
    run2()
    # 시간 체크
    T -= 1


# 미세먼지 값
result = 0
for i in range(N):
    for j in range(M):
        if maps[i][j] > 0:
            result += maps[i][j]

print(result)