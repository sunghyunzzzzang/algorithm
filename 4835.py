T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    M_sum_max = 0
    M_sum_min = 0
    M_sum = 0

    for i in range(N-M+1):
        for j in range(i,i+M):
            M_sum += arr[j]

        if i == 0:
            M_sum_max = M_sum
            M_sum_min = M_sum

        if M_sum > M_sum_max:
            M_sum_max = M_sum
        if M_sum < M_sum_min:
            M_sum_min = M_sum

        M_sum = 0

    result = M_sum_max - M_sum_min
    print('#{} {}'.format(test_case, result))