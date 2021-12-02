# 16935. 배열 돌리기 3

import copy

def run1():
    global maps, N, M
    R = N - 1
    C = M - 1
    temp = [[0] * M for i in range(N)]

    for i in range(N):
        for j in range(M):
            temp[i][j] = maps[R-i][j]
    """
    # ex2)
    for i in range(N):
        temp[i][:M] = maps[R-i][:M]
    """
    maps = copy.deepcopy(temp)

def run2():
    global maps, N, M
    R = N - 1
    C = M - 1
    temp = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = maps[i][C - j]

    maps = copy.deepcopy(temp)

def run3():
    global maps, N, M
    R = N - 1
    C = M - 1
    # 배열을 N, M 반대로 만들어줌
    temp = [[0] * N for i in range(M)]
    # M, N을 반대로
    for i in range(M):
        for j in range(N):
            temp[i][j] = maps[R-j][i]

    maps = copy.deepcopy(temp)
    N, M = M, N

def run4():
    global maps, N, M
    R = N - 1
    C = M - 1
    # 배열을 N, M 반대로 만들어줌
    temp = [[0] * N for i in range(M)]
    # M, N을 반대로
    for i in range(M):
        for j in range(N):
            temp[i][j] = maps[j][C - i]

    maps = copy.deepcopy(temp)
    N, M = M, N

def run5():
    global maps, N, M
    R = N - 1
    C = M - 1
    temp = [[0] * M for i in range(N)]
    R_mid = N//2
    C_mid = M//2

    """
    # ex2) 1번그룹 -> 2번그룹
    for i in range(R_mid):
        temp[i][R_mid+1:M] = maps[i][:R_mid+1]
    """

    # 1번그룹 -> 2번그룹
    for i in range(R_mid):
        for j in range(C_mid):
            temp[i][C_mid + j] = maps[i][j]

    # 2번그룹 -> 3번그룹
    for i in range(R_mid):
        for j in range(C_mid, M):
            temp[R_mid + i][j] = maps[i][j]
    
    # 3번그룹 -> 4번그룹
    for i in range(R_mid, N):
        for j in range(C_mid, M):
            temp[i][j-C_mid] = maps[i][j]

    # 4번그룹 -> 1번그룹
    for i in range(R_mid, N):
        for j in range(C_mid):
            temp[i - R_mid][j] = maps[i][j]

    maps = copy.deepcopy(temp)

def run6():
    global maps, N, M
    R = N - 1
    C = M - 1
    temp = [[0] * M for i in range(N)]
    R_mid = N//2
    C_mid = M//2

    # 2번그룹 -> 1번그룹
    for i in range(R_mid):
        for j in range(C_mid):
            temp[i][j] = maps[i][C_mid + j]

    # 3번그룹 -> 2번그룹
    for i in range(R_mid):
        for j in range(C_mid, M):
            temp[i][j] = maps[R_mid + i][j]

    # 4번그룹 -> 3번그룹
    for i in range(R_mid, N):
        for j in range(C_mid, M):
            temp[i][j] = maps[i][j - C_mid]

    # 1번그룹 -> 4번그룹
    for i in range(R_mid, N):
        for j in range(C_mid):
            temp[i][j] = maps[i - R_mid][j]

    maps = copy.deepcopy(temp)

N, M, R = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
command = list(map(int, input().split()))

for cmd in command:
    # 상하 반전
    if cmd == 1:
        run1()
    # 좌우 반전
    elif cmd == 2:
        run2()
    # 시계방향 90도 회전
    elif cmd == 3:
        run3()
    # 반시계방향 90도 회전
    elif cmd == 4:
        run4()
    # 그룹이동
    elif cmd == 5:
        run5()
    # 5번 그룹이동 반대로
    elif cmd == 6:
        run6()

# 출력
for i in range(N):
    print(*maps[i])