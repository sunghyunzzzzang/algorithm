# 5105. 미로의거리
# BFS
# 재귀
import sys
sys.stdin = open("input.txt", "r")

def bfs(x, y):
    global result
    x_start, y_start = queue.pop(0)
    if maze[x][y] == 3:
        result = distance[x][y] - 1
        return
    else:
        for i in range(4):
            nx = x_start + dx[i]
            ny = y_start + dy[i]
            if nx in range(N) and ny in range(N) and maze[nx][ny] != 1 and visited[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                bfs(nx, ny)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    flag = 0
    # N: 배열크기
    N = int(input())
    visited = [[0] * N for i in range(N)]
    maze = []
    queue = []
    distance = [[0] * N for i in range(N)]
    for i in range(N):
        maze.append(list(map(int, list(input()))))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x_start = i
                y_start = j

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue.append((x_start, y_start))
    visited[x_start][y_start] = 1

    bfs(x_start, y_start)

    print('#{} {}'.format(test_case, result))