#4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N: 칠할 영역의 개수
    N = int(input())
    # K: 배열 크기
    K = 10
    arr = [[0] * K for i in range(K)]
    result = 0

    # 색칠
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        #[2,2]에서 [4,4]까지 색칠하려면 x2, y2에 +1을 더해줌
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                arr[x][y] += color

    # 겹쳐서 색이 칠해진 칸
    for i in range(K):
        for j in range(K):
            if arr[i][j] == 3:
                result += 1

    print('#{} {}'.format(test_case, result))