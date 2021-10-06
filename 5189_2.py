# 5189. 전자카트
from itertools import permutations
import sys
sys.stdin = open("input.txt", "r")

def dfs():
    last_x = 0
    global temp, result

    for i in range(len(per)):
        for j in range(len(per[i])):
            nx = per[i][j]
            ny = per[i][j]
            temp += arr[last_x][ny]
            last_x = nx

            # 최소값을 넘으면
            if result < temp:
                break

        # 마지막에 출발지 더해줌
        temp += arr[last_x][0]
        if result > temp:
            result = temp

        last_x = 0
        temp = 0

    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(list(map(int, input().split())))

    idx = [i for i in range(1, N)]
    per = list(permutations(idx))

    temp = 0
    result = 999999

    dfs()

    print("#{} {}".format(test_case, result))