# 3190. 뱀

from collections import deque

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

turn = {
    'L' : 3,
    'D' : 1
}

def run(x, y, direction):
    time = 0
    # 뱀 처음 위치 넣기
    snake.append((x, y))

    while 1:
        head_x, head_y = snake[-1]

        # 방향 전환 커맨드가 있으면
        if len(move) == 0:
            pass
        else:
            # 해당 시간에 방향 전환 커맨드 사용
            if time == int(move[0][0]):
                # 왼쪽으로 회전하면
                if move[0][1] == 'L':
                    direction = (direction + turn['L']) % 4
                # 오른쪽으로 회전하면
                elif move[0][1] == 'D':
                    direction = (direction + turn['D']) % 4
                # 사용한 커맨드 제거
                move.popleft()

        # 이동할 위치
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]

        # 벽에 부딪치면 종료
        if not nx in range(N) or not ny in range(N):
            return time + 1
        # 내 몸에 닿으면 종료
        if (nx, ny) in snake:
            return time + 1
        # 이동 할 위치에 사과가 있다면, 꼬리가 길어지고 한 칸 이동 and 사과 제거
        if maps[nx][ny] == 2:
            maps[nx][ny] = 0
            snake.append((nx, ny))
        # 이동 할 위치에 사과가 없다면, 한 칸 이동
        else:
            snake.append((nx, ny))
            snake.popleft()

        time += 1





# N*N maps 크기
N = int(input())
# 사과의 개수
K = int(input())
maps = [[0] * N for i in range(N)]

# 뱀 크기
snake = deque()

# 사과 생성
for i in range(K):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 2

# 이동
L = int(input())
move = deque()
for i in range(L):
    x, y = input().split()
    move.append((x, y))

result = run(0, 0, 1)
print(result)