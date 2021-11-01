# 23288. 주사위 굴리기 2

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 해당 칸에 도착했을 때 점수 계산
def bfs(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    visited = [[0] * M for i in range(N)]
    visited[s_x][s_y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] != 0:
                continue
            # 같은 값인지 체크
            if maps[nx][ny] != maps[x][y]:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1

    return sum(map(sum, visited)) * maps[s_x][s_y]

# 북 서 남 동
def change(dir):
    # 북
    if dir == 0:
        dice[1], dice[2], dice[3], dice[4] = dice[4], dice[1], dice[2], dice[3]
    # 서
    elif dir == 1:
        dice[1], dice[3], dice[5], dice[6] = dice[5], dice[6], dice[3], dice[0]
    # 남
    elif dir == 2:
        dice[1], dice[2], dice[3], dice[4] = dice[2], dice[3], dice[4], dice[1]
    # 동
    elif dir == 3:
        """
        dice[1] = dice[6]
        dice[3] = dice[5]
        dice[5] = dice[0]
        dice[6] = dice[3]
        """
        dice[1], dice[3], dice[5], dice[6] = dice[6], dice[5], dice[0], dice[3]


N, M, K = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

dice = [0, 1, 5, 6, 2, 4, 3]

# 초기 좌표 및 방향 설정(동쪽)
x = 0
y = 0
dir = 3

result = 0
for i in range(K):
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 범위 넘어가면 반대 방향으로 가기
    if not nx in range(N) or not ny in range(M):
        dir = (dir + 2) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    result += bfs(nx, ny)

    change(dir)
    bottom = dice[3]
    # 시계 방향 회전
    if bottom > maps[nx][ny]:
        dir = (dir + 3) % 4
    # 반시계 방향 회전
    elif bottom < maps[nx][ny]:
        dir = (dir + 1) % 4

    x = nx
    y = ny

print(result)