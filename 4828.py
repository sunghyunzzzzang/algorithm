T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    count = int(input())
    arr = list(map(int, input().split()))

    max = arr[0]
    min = arr[0]

    for i in range(1, count):
        if arr[i] > max:
            max = arr[i]
        elif min > arr[i]:
            min = arr[i]


    print("#", test_case, " ", max-min, sep="")
    #print('#{} {}'.format(test_case, (max-min)))