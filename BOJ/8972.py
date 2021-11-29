# 8972. 미친 아두이노

import copy
from collections import deque

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

def mad_arduino():
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'R':
                min_dist = []
                # 8방향에 대해 체크
                for d in range(1, 10):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    # 배열 크기 체크
                    if nx not in range(N) or ny not in range(M):
                        continue
                    dist = abs(x-nx) + abs(y-ny)
                    min_dist.append((dist, nx, ny))
                # 가장 가까운 거리순으로 정렬
                min_dist.sort()
                min_x = min_dist[0][1]
                min_y = min_dist[0][2]
                # 종수의 아두이노를 만나면
                if temp[min_x][min_y] == 'I':
                    return -1
                # 2개 이상 미친 아두이노가 같은 칸에 있는 경우 boom에 좌표를 넣어둠
                if temp[min_x][min_y] == 'R':
                    boom.append((min_x, min_y))
                temp[min_x][min_y] = 'R'
    return 0

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(input()))
command = deque(list(input()))
command_len = len(command)

for i in range(N):
    for j in range(M):
        if maps[i][j] == 'I':
            x = i
            y = j
cnt = 0
boom = deque()

while command:
    cnt += 1
    cmd = int(command.popleft())

    # 종수의 아두이노 이동
    nx = x + dx[cmd]
    ny = y + dy[cmd]
    if maps[nx][ny] == 'R':
        break
    maps[nx][ny] = 'I'
    maps[x][y] = '.'
    x = nx
    y = ny

    # mad_arduino를 temp에서 이동하게 만듬
    temp = [['.'] * M for i in range(N)]
    temp[x][y] = 'I'
    # 미친 아두이노 이동
    check = mad_arduino()

    # 미친 아두이노가 종수의 아두이노를 만나면
    if check == -1:
        break

    # 2개 이상 미친 아두이노가 같은 칸에 있는 경우 폭발해 없어짐
    while boom:
        boom_x, boom_y = boom.popleft()
        temp[boom_x][boom_y] = '.'

    maps = copy.deepcopy(temp)

# 출력
if command_len == cnt:
    for i in range(N):
        print("".join(maps[i]))
else:
    print('{} {}'.format('kraj', cnt))