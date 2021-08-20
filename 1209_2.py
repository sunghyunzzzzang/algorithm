import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    # 배열 크기
    N = 100
    arr = [[0] * N for i in range(N)]
    Max = 0
    Sum_row = 0
    Sum_col = 0
    Sum_a = 0
    Sum_b = 0

    # 배열 값 입력
    for i in range(N):
        arr[i] = (list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            Sum_row += arr[i][j]  # Row Sum
            Sum_col += arr[j][i]  # Col Sum

        Max = max(Max, Sum_row, Sum_col)
        Sum_row = 0
        Sum_col = 0

        Sum_a += arr[i][i]  # arr[0][0] ~ arr[99][99]
        Sum_b += arr[(N - 1) - i][i]  # arr[99][0] ~ arr[0][99]

    Max = max(Max, Sum_a, Sum_b)

    print('#{} {}'.format(number, Max))