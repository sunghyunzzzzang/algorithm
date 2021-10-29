# 1018. 체스판 다시 칠하기

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(input())

result = 100000
for dx in range(0, N-7):
    for dy in range(0, M-7):
        cnt1 = 0
        cnt2 = 0
        for i in range(dx, dx+8):
            for j in range(dy, dy+8):
                # 짝수 Row (0,j)
                if i % 2 == 0:
                    # 짝수 Col (0,0)
                    if j % 2 == 0:
                        # (0,0)이 'B'로 시작할 때 = (0,1)이 'W'로 시작할 때
                        if maps[i][j] == 'B':
                            cnt1 += 1
                        # (0,0)이 'W'로 시작할 때 = (0,1)이 'B'로 시작할 때
                        else:
                            cnt2 += 1
                    # 홀수 Col (0,1)
                    else:
                        # (0,0)이 'B'로 시작할 때 = (0,1)이 'W'로 시작할 때
                        if maps[i][j] == 'W':
                            cnt1 += 1
                        # (0,0)이 'W'로 시작할 때 = (0,1)이 'B'로 시작할 때
                        else:
                            cnt2 += 1
                # 홀수 Row (1,j)
                else:
                    if j % 2 == 0:
                        if maps[i][j] == 'W':
                            cnt1 += 1
                        else:
                            cnt2 += 1
                    else:
                        if maps[i][j] == 'B':
                            cnt1 += 1
                        else:
                            cnt2 += 1

        result = min(result, cnt1, cnt2)

print(result)