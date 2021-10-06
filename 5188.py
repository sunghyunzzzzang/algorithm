# 5188. 최소합
import sys
sys.stdin = open("input.txt", "r")

def dfs(x, y):
    #우, 하
    dx = [1, 0]
    dy = [0, 1]

    global temp, result

    # 최소값을 넘으면 return
    if result < temp:
        return
    # 도착
    if x == N - 1 and y == N - 1:
        result = temp
        return
    # 우, 하 탐색
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                temp += arr[nx][ny]
                dfs(nx, ny)
                # 나오면서 값 다시 뺴줌
                temp -= arr[nx][ny]


TC = int(input())

for test_case in range(1, TC + 1):
    # N: 배열 크기
    N = int(input())
    result = 9999999
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 시작 좌표
    x, y = 0, 0
    # 시작 좌표에 해당하는 값 저장
    temp = arr[x][y]
    dfs(x, y)

    print("#{} {}".format(test_case, result))