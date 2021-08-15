T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    #평탄화 작업
    for i in range(N):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1

    #결과
    result = max(arr) - min(arr)
    print('#{} {}'.format(test_case, result))