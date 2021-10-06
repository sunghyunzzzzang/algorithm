# 5189. 전자카트

#import sys
#sys.stdin = open("input.txt", "r")

def dfs(x, temp):
    global result, cnt

    if cnt == N - 1:
        temp += arr[x][0]
        if result > temp:
            result = temp
        return

    for i in range(1, N):
        nx = i
        ny = i
        if 1 <= nx < N and 1 <= ny < N and visited[ny] == 0:
            temp += arr[x][ny]
            visited[ny] = 1
            cnt += 1
            dfs(nx, temp)
            temp -= arr[x][ny]
            visited[ny] = 0
            cnt -= 1



T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0 for i in range(N)]
    temp = 0
    result = 999999
    cnt = 0
    x, y = 0, 0

    dfs(x, temp)

    print("#{} {}".format(test_case, result))