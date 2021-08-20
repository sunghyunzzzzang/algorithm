import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    N = 100
    arr = [[0] * N for i in range(N)]
    Max = 0
    Sum = 0
    Sum_b = 0

    # 배열 값 입력
    for i in range(N):
        arr[i] = (list(map(int, input().split())))

    #Row Sum
    for i in range(N):
        for j in range(N):
            Sum += arr[i][j]

        #최대값 비교
        if Sum > Max:
            Max = Sum
        Sum = 0

    #Col Sum
    for j in range(N):
        for i in range(N):
            Sum += arr[i][j]

        #최대값 비교
        if Sum > Max:
            Max = Sum
        Sum = 0


    for i in range(N):
        Sum += arr[i][i]            # arr[0][0] ~ arr[99][99]
        Sum_b += arr[(N-1)-i][i]    # arr[99][0] ~ arr[0][99]

    result = max(Sum, Sum_b, Max)

    print('#{} {}'.format(number, result))