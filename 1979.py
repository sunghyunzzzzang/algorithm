#1979. 어디에 단어가 들어갈 수 있을까
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N: 배열크기, K: 들어갈 문자열 길이
    N, K = map(int, input().split())
    arr = []
    cnt = 0
    result = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        #행
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if N == j+1 or arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
        #열
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if N == j+1 or arr[j][i] == 0:
                if cnt == K:
                    result += 1
                cnt = 0

    print('#{} {}'.format(test_case, result))