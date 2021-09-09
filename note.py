#2차원 배열 받을 때 (NO Split)
# input
"""
5
13101
10101
10101
10101
10021
"""
# 방법 1
N = int(input())
maze = [list(map(int, list(input()))) for _ in range(N)]

# 방법 2
N = int(input())
maze = []

for i in range(N):
    maze.append(list(map(int, list(input()))))

# 방법 3
maze = [[0] * N for i in range(N)]
for i in range(N):
    maze[i] = list(map(int, input()))


#2차원 배열 0으로 초기화
visited = [[0] * N for i in range(N)]


# 사방탐색
if nx in range(N) and ny in range(N):
    stack.append((nx, ny))
    visited[nx][ny] = 1
else:
    continue