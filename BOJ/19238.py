# 19238. 스타트 택시

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global move, cur_start_x, cur_start_y,cur_end_x, cur_end_y
    q = deque()
    q.append((x, y))
    visited = [[0] * N for i in range(N)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 배열 크기 체크
            if nx not in range(N) or ny not in range(N):
                continue
            # 방문 체크
            if visited[nx][ny] != 0:
                continue
            # 벽 체크
            if maps[nx][ny] == 1:
                continue
            # 빈 공간일 때
            elif maps[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            # 최단거리 승객
            else:
                move = visited[x][y]
                cur_start_x, cur_start_y = nx, ny
                cur_end_x, cur_end_y = maps[nx][ny]
                maps[nx][ny] = 0
                return
    return -1

# N : 배열 크기, M : 승객 수, fuel : 연료
N, M, fuel = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

x, y = map(int, input().split())
start_x = x-1
start_y = y-1

for i in range(M):
    s_x, s_y, e_x, e_y = map(int, input().split())
    maps[s_x-1][s_y-1] = (e_x-1, e_y-1)

for i in range(M):
    move = 0
    cur_start_x = 0
    cur_start_y = 0
    cur_end_x = 0
    cur_end_y = 0

    check = bfs(start_x, start_y)
    # 다음 출발지나 목적지 이동할 수 없으면
    if check == -1:
        print(-1)
        fuel = 0
        break

    # 출발지에서 승객탑승까지 연료 계산
    fuel -= move
    # 승객탑승에서 도착지까지 연료 계산
    fuel -= (abs(cur_start_x - cur_end_x) + abs(cur_start_y - cur_end_y))

    # 연료가 바닥 났을 때
    if fuel <= 0:
        print(-1)
        break

    # 승객을 태워서 도착 시 연료 두 배 충전
    fuel += 2 * (abs(cur_start_x - cur_end_x) + abs(cur_start_y - cur_end_y))
    # 도착지를 시작 지점으로
    start_x, start_y = cur_end_x, cur_end_y

if fuel >= 1:
    print(fuel)