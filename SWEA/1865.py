# 1865. 동철이의 일 분배

#import sys
#sys.stdin = open("input.txt", "r")

def dfs(s, prob):
    global result, cnt

    # 최대확률보다 현재 확률이 작으면 // 곱하는 값이 1보다 작기때문에
    if prob <= result:
        return

    # 배열 끝까지 돌았을 때
    if cnt == N:
        if result < prob:
            result = prob
        return


    for i in range(N):
        # 방문하지 않은 곳 체크
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(s + 1, (prob * arr[s][i] / 100))
            visited[i] = 0
            cnt -= 1

T = int(input())
for test_case in range(1, T + 1):
    # N: 배열 크기
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    visited = [0 for i in range(N)]

    # s: start, prob: 확률, cnt: count
    result = 0
    s = 0
    prob = 1
    cnt = 0
    dfs(s, prob)

    print("#{} {:6f}".format(test_case, result * 100))