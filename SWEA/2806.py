# 2806. N-Queen

import sys
sys.stdin = open("input.txt", "r")

def dfs(s, count, arr):
    global result

    # 퀸을 다 놓게 되면
    if count == 0:
        result += 1

    # 행 별로 확인
    for i in range(N):
        x = s
        y = i

        # 방문하지않은 열 and 공격범위가 아니면
        if visited[i] == 0 and arr[s][i] == 0:
            visited[i] = 1

            # arr에 대각선 범위 체크  // 재귀를 사용해 행마다 퀸 1개씩 놓고 visited를 사용해 열마다 퀸 1개씩 놓으므로 대각선만 체크해줌
            for j in range(N):
                if x + j in range(N) and y + j in range(N):
                    arr[x + j][y + j] += 1
                if x - j in range(N) and y - j in range(N):
                    arr[x - j][y - j] += 1
                if y + j in range(N) and x - j in range(N):
                    arr[x - j][y + j] += 1
                if x + j in range(N) and y - j in range(N):
                    arr[x + j][y - j] += 1

            dfs(s+1, count-1, arr)

            # arr에 대각선 범위 체크 없애기
            for j in range(N):
                if x + j in range(N) and y + j in range(N):
                    arr[x + j][y + j] -= 1
                if x - j in range(N) and y - j in range(N):
                    arr[x - j][y - j] -= 1
                if y + j in range(N) and x - j in range(N):
                    arr[x - j][y + j] -= 1
                if x + j in range(N) and y - j in range(N):
                    arr[x + j][y - j] -= 1

            visited[i] = 0



TC = int(input())
for test_case in range(1, TC + 1):
    # N: 배열크기 , count: 퀸 개수
    N = int(input())
    count = N
    # arr: 체스판 , visited: 열 체크
    arr = [[0] * N for i in range(N)]
    visited =[0] * N
    # result : 경우의 수 저장 , s : 시작 행
    result = 0
    s = 0

    dfs(s, count, arr)

    print("#{} {}".format(test_case, result))