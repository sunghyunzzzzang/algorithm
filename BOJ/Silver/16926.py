# 16926. 배열 돌리기 1

# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for cmd in range(R):
    visited = [[0] * M for i in range(N)]

    len = min(N, M) // 2
    for s_index in range(len):
        s_x = s_index
        s_y = s_index

        # 마지막에 값 넣어주기 위해 저장
        temp = arr[s_x][s_y]

        x = s_x
        y = s_y
        dir = 0
        while 1:
            # 4방향 다 돌면 멈춤
            if dir == 4:
                break
            nx = (x + dx[dir])
            ny = (y + dy[dir])
            # 배열 범위 체크
            if nx not in range(N) or ny not in range(M):
                dir += 1
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                dir += 1
                continue
            arr[x][y] = arr[nx][ny]
            visited[x][y] = 1
            x = nx
            y = ny

        # 처음 위치 값을 마지막에 넣어줌
        arr[x][y] = temp

# 출력
for i in range(N):
    print(*arr[i])