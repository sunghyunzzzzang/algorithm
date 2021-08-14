T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    aj = list(map(int, input()))
    arr = [0 for i in range(10)]

    for i in range(N):
        arr[aj[i]] += 1

    max_count = arr[0]
    max_number = 0
    for i in range(1, 10):
        if arr[i] >= max_count:
            max_count = arr[i]
            max_number = i

    print('#{} {} {}'.format(test_case, max_number, max_count))