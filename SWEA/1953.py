# 1953. 탈주범 검거

import sys
sys.stdin = open("input.txt", "r")

tunnel = {
    0 : (),
    1 : ((-1, 0), (1, 0), (0, -1), (0, 1)),  # 상 하 좌 우
    2 : ((-1, 0), (1, 0)),  # 상 하
    3 : ((0, -1), (0, 1)),  # 좌 우
    4 : ((-1, 0), (0, 1)),  # 상 우
    5 : ((1, 0), (0, 1)),   # 하 우
    6 : ((0, -1), (1, 0)),  # 좌 하
    7 : ((0, -1), (-1, 0))  # 좌 상
}


def BFS(x, y, L):
    global result
    queue = []
    queue.append((x, y))
    visited[x][y] = 1


    while queue:
        x, y = queue.pop(0)
        result += 1

        if visited[x][y] >= L:
            continue

        # 현재 좌표의 터널모양을 가져옴
        for (dx, dy) in tunnel[Map[x][y]]:
            nx = x + dx
            ny = y + dy
            if nx in range(N) and ny in range(M) and visited[nx][ny] == 0 and Map[nx][ny] != 0:
                # 다음 좌표의 터널과 연결이 되면
                if (-dx, -dy) in tunnel[Map[nx][ny]]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))




TC = int(input())
for test_case in range(1, TC + 1):
    # N: 세로크기, M: 가로크기, R: 맨홀 뚜껑 Row, C: 맨홀 뚜껑 Col, L: 소요된 시간
    N, M, R, C, L = map(int, input().split())
    # Map : 지하 터널 지도
    Map = []
    for i in range(N):
        Map.append(list(map(int, input().split())))
    visited = [[0] * M for i in range(N)]
    result = 0

    BFS(R, C, L)

    print("#{} {}".format(test_case, result))
