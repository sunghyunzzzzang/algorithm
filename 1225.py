#4866. 암호생성기
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    TC = int(input())
    arr = list(map(int, input().split()))

    #배열 마지막 자리가 0보다 작을 때 까지 반복
    while arr[-1] > 0:
        # Cycle
        for i in range(5):
            Move = arr[0]
            Move = Move - (i + 1)

            # 맨 뒤로 옮기는 숫자가 0보다 작거나 같으면 0
            if Move <= 0:
                Move = 0

            arr.pop(0)
            arr.append(Move)

            # 맨 뒤로 옮기는 숫자가 0보다 작거나 같으면 암호 도출
            if Move <= 0:
                break

    #출력
    print('#{} '.format(test_case), end='')
    for i in arr:
        print(i, end=' ')
    print()