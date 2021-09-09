#4875. 미로
# DFS
# 재귀
import sys
sys.stdin = open("input.txt", "r")

def dfs(x, y):
    global result

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == 1:
            continue
        visited[nx][ny] = 1

        if maze[nx][ny] == 0:
            dfs(nx, ny)
        if maze[nx][ny] == 3:
            result = 1
            return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    maze = []
    result = 0
    visited = [[0] * N for i in range(N)]

    for i in range(N):
        maze.append(list(map(int, list(input()))))

    # 시작지점 index 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x_start = i
                y_start = j

    #상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]

    dfs(x_start, y_start)
    print('#{} {}'.format(test_case, result))