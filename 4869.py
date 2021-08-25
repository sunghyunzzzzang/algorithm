#4869. 종이붙이기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0, 1, 3]

    for i in range(3, int(N/10)+1):
        # 계산식
        # a[2] = (a[0] * 2) + a[1]
        arr.append(arr[i-2]*2 + arr[i-1])

    print('#{} {}'.format(test_case, arr[-1]))