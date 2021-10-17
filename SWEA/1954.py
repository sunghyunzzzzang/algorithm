# 1954. 달팽이 숫자

#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for i in range(N)]

    # 우 하 좌 상
    dx = [0, 1, 0 , -1]
    dy = [1, 0, -1, 0]

    cnt = 1
    x = 0
    y = 0
    i = 0

    arr[x][y] = cnt

    while cnt < N*N:
        nx = x + dx[i]
        ny = y + dy[i]

        # 배열 값 범위를 넘어갈 때
        if not nx in range(N) or not ny in range(N):
            i = (i+1) % 4
            continue
        # 이미 방문한 곳 일때
        if arr[nx][ny] != 0:
            i = (i + 1) % 4
            continue

        x = nx
        y = ny
        cnt += 1
        arr[x][y] = cnt

    print("#{}".format(tc))
    for i in range(N):
        print(*arr[i])