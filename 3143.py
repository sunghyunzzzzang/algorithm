#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0

    str_a, str_b = input().split()
    i = 0

    while i < len(str_a):
        #문자열 비교
        if str_a[i:i+len(str_b)] == str_b:
            i = i + len(str_b)
            answer += 1
        else:
            i = i+1
            answer += 1

    print('#{} {}'.format(test_case, answer))