# 20056. 마법사 상어와 파이어볼
import copy
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
maps = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    maps[r - 1][c - 1].append([m, s, d])

for k in range(K):
    temp = [[deque() for _ in range(N)] for _ in range(N)]
    # 파이어볼 이동
    for i in range(N):
        for j in range(N):
            # 파이어볼이 있으면
            while maps[i][j]:
                m, s, d = maps[i][j].popleft()
                nx = (i + (s * dx[d])) % N
                ny = (j + (s * dy[d])) % N
                temp[nx][ny].append([m, s, d])

    maps = copy.deepcopy(temp)

    # 파이어볼 합치기
    for i in range(N):
        for j in range(N):
            # 파이어볼이 2개 이상이면
            if len(maps[i][j]) >= 2:
                odd = False
                even = False
                sum_m = 0
                sum_s = 0
                count = len(maps[i][j])

                while maps[i][j]:
                    m, s, d = maps[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        even = True
                    else:
                        odd = True

                # 질량 속력 계산
                sum_m = sum_m // 5
                sum_s = sum_s // count

                # 질량 0이면 소멸
                if sum_m <= 0:
                    continue

                # 홀수 짝수 둘 다 있으면
                if odd == True and even == True:
                    for d in range(1, 8, 2):
                        maps[i][j].append([sum_m, sum_s, d])
                else:
                    for d in range(0, 8, 2):
                        maps[i][j].append([sum_m, sum_s, d])

result = 0
for i in range(N):
    for j in range(N):
        while maps[i][j]:
            m, s, d = maps[i][j].popleft()
            result += m

print(result)