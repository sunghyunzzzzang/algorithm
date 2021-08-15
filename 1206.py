T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    second_height = 0
    ssum = 0


    for i in range(2, N-2):
        #왼쪽 2칸 오른쪽 2칸
        for j in range(i-2, i+3):
            #현재 빌딩
            if i == j:
                continue
            #주변 빌딩보다 현재 빌딩이 높을 때
            if arr[i] > arr[j]:
                #주변 빌딩 Max찾기
                if arr[j] > second_height:
                    second_height = arr[j]
            #현재 빌딩이 높을 때
            else:
                second_height = arr[i]

        ssum += arr[i] - second_height
        second_height = 0

    print('#{} {}'.format(test_case, ssum))