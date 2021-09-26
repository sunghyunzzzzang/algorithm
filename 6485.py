#6485. 삼성시의 버스 노선
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N: 버스노선, arr: 버스정류장
    N = int(input())
    arr = [0 for i in range(5001)]

    # A: Start Station, B: End Station
    # 버스 정류장을 지나는 버스 노선의 개수 구하기
    for i in range(N):
        A, B = map(int, input().split())
        for k in range(A, B+1):
            arr[k] += 1

    # 버스 정류장 출력 개수
    P = int(input())

    print('#{}'.format(test_case), end='')
    for i in range(P):
        C = int(input())
        print("", arr[C], end='')
    print()