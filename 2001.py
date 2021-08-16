T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    result = 0
    Max = 0

    for k in range(N):
        arr.append(list(map(int, input().split())))

    #배열
    for x in range(N-M+1):
        for y in range(N-M+1):
            #파리채
            for i in range(M):
                for j in range(M):
                    result += arr[x+i][y+j]

            if result > Max:
                Max = result
            result = 0

    print('#{} {}'.format(test_case, Max))