#4865. 글자수
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str_a = input()
    str_b = input()
    cnt = 0
    Max = 0

    for i in range(len(str_a)):
        for j in range(len(str_b)):
            if str_a[i] == str_b[j]:
                cnt += 1

        if cnt > Max:
            Max = cnt
        cnt = 0

    print('#{} {}'.format(test_case, Max))