# 14499. 주사위 굴리기
"""
동쪽으로 굴릴 때
dice[0][0] = dice[0][1]
dice[0][1] = dice[2][0]
dice[2][0] = dice[0][2]
dice[0][2] = dice[0][0]
"""

def change(command):
    # 동
    if command == 1:
        dice[0][0], dice[0][1], dice[2][0], dice[0][2] = dice[0][1], dice[2][0], dice[0][2], dice[0][0]
    # 서
    elif command == 2:
        dice[0][0], dice[0][1], dice[2][0], dice[0][2] = dice[0][2], dice[0][0], dice[0][1], dice[2][0]
    # 북
    elif command == 3:
        dice[0][0], dice[3][0], dice[2][0], dice[1][0] = dice[3][0], dice[2][0], dice[1][0], dice[0][0]
    # 남
    elif command == 4:
        dice[0][0], dice[1][0], dice[2][0], dice[3][0] = dice[1][0], dice[2][0], dice[3][0], dice[0][0]


# 동 서 북 남
dir = {
    1: [0, 1],
    2: [0, -1],
    3: [-1, 0],
    4: [1, 0]
}

N, M, x, y, K = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

command = list(map(int, input().split()))
dice = [[0] * 3 for i in range(4)]
# 주사위 굴리기
for k in range(K):
    cur_command = dir[command[k]]
    nx = x + cur_command[0]
    ny = y + cur_command[1]
    # 범위 체크
    if not nx in range(N) or not ny in range(M):
        continue

    # 주사위 바닥면 바꿈
    change(command[k])
    # 이동 할 좌표가 0이면
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[0][0]
    # 이동 할 좌표에 값이 있으면
    else:
        dice[0][0] = maps[nx][ny]
        maps[nx][ny] = 0

    # 출력
    print(dice[2][0])

    x = nx
    y = ny