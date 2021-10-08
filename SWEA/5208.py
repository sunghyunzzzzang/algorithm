# 5208. 전기버스2

import sys
sys.stdin = open("input.txt", "r")

def dfs(s, count):
    global result, N

    if result < count:
        return

    if s >= N:
        result = count
        return

    else:
        # 정류장에서 가장 멀리갈수 있는 곳부터 확인
        for i in range(station[s], 0, -1):
            if visited[s] == 0:
                visited[s] = 1
                dfs(s+i, count+1)
                visited[s] = 0


TC = int(input())
for test_case in range(1, TC + 1):
    # station: 정류장 // [1]부터 사용
    station = list(map(int, input().split()))
    # N: 도착정류장번호
    N = station[0]
    visited = [0] * N

    result = 999999
    s = 1
    # 변경한 횟수 // 1번 정류장에서 다음정류장으로 갈 때 교체하기때문에 -1 넣어줌
    count = -1

    dfs(s, count)

    print("#{} {}".format(test_case, result))