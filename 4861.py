#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N = 배열 크기, M = 찾을 문자열 크기
    N, M = map(int, input().split())

    cnt = 0
    answer = [0 for i in range(M)]
    arr = [[x for x in input()] for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            exi = []
            exj = []
            for k in range(M):
                exi += arr[i][j+k]
                exj += arr[j+k][i]


            if exi == exi[::-1]:
                answer = "".join(exi)
                break
            if exj == exj[::-1]:
                answer = "".join(exj)
                break

    print('#{} {}'.format(test_case, answer))