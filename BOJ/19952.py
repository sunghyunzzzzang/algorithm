# 19952. 인성 문제 있어??

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s_x, s_y, e_x, e_y, F):
    q.append((s_x, s_y, F))
    visited[s_x][s_y] = 1

    while q:
        x, y, F = q.popleft()

        # 힘이 다하면
        if F <= 0:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if nx not in range(N) or ny not in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] != 0:
                continue
            # 현재 위치보다 낮은 곳으로 갈 때
            if maps[x][y] >= maps[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, F-1))
            # 현재 위치보다 높은 곳으로 갈 때
            elif maps[nx][ny] > maps[x][y]:
                if maps[nx][ny] - maps[x][y] <= F:
                    visited[nx][ny] = 1
                    q.append((nx, ny, F-1))

            # 목적지 도착
            if nx == e_x and ny == e_y:
                return 1

    return -1

tc = int(input())
for test_case in range(1, tc+1):
    N, M, O, F, s_x, s_y, e_x, e_y = map(int, input().split())
    maps = [[0] * M for i in range(N)]

    good = "잘했어!!"
    bad = "인성 문제있어??"

    for i in range(O):
        X, Y, L = map(int, input().split())
        maps[X-1][Y-1] = L

    s_x -= 1
    s_y -= 1
    e_x -= 1
    e_y -= 1

    q = deque()
    visited = [[0] * M for i in range(N)]
    check = bfs(s_x, s_y, e_x, e_y, F)

    # 목적지 도착
    if check == 1:
        print(good)
    # 목적지 도착 X
    else:
        print(bad)