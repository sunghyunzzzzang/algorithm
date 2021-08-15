T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        arr_max = arr[0]
        arr_min = arr[0]
        max_index = 0
        min_index = 0

        for j in range(1, len(arr)):
            # arr[j]가 더 클때
            if arr_max < arr[j]:
                arr_max = arr[j]
                max_index = j
            # arr[j]가 더 작을때
            if arr_min > arr[j]:
                arr_min = arr[j]
                min_index = j

        arr[max_index] -= 1
        arr[min_index] += 1


    arr_max = arr[0]
    arr_min = arr[0]
    for j in range(1, len(arr)):
        # arr[j]가 더 클때
        if arr_max < arr[j]:
            arr_max = arr[j]
        # arr[j]가 더 작을때
        if arr_min > arr[j]:
            arr_min = arr[j]


    result = arr_max - arr_min
    print('#{} {}'.format(test_case, result))