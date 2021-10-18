# 1012. 유기농 배추

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = []
    q.append((x, y))
    maps[x][y] = 0
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 배열 범위 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                continue
            # 배추 체크
            if maps[nx][ny] == 0:
                continue
            visited[nx][ny] = 1
            # 방문한 곳 배추 없애줌
            maps[nx][ny] = 0
            q.append((nx, ny))

TC = int(input())
for tc in range(1, TC + 1):
    # M: 세로, N: 가로, K: 좌표 개수
    M, N, K = map(int, input().split())
    maps = [[0] * M for i in range(N)]
    visited = [[0] * M for i in range(N)]
    result = 0

    # maps에 배추 표시
    for i in range(K):
        y, x = map(int, input().split())
        maps[x][y] = 1

    # 배추 찾기
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)