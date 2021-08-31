#4875. 미로
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    maze = []
    stack = []
    visited = [[0] * N for i in range(N)]

    for i in range(N):
        maze.append(list(map(int, list(input()))))

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #시작지점 index 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x_start = i
                y_start = j

    #시작지점
    visited[x_start][y_start] = 1
    stack.append((x_start, y_start))


    while stack:
        x_start, y_start = stack.pop()
        #탈출
        if maze[x_start][y_start] == 3:
            result = 1
            break
        else:
            for i in range(4):
                nx = x_start + dx[i]
                ny = y_start + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny] == 1 or maze[nx][ny] == 1:
                    continue
                else:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1

    print('#{} {}'.format(test_case, result))