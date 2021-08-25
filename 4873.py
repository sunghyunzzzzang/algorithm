#4873. 반복문자 지우기
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str = input()
    stack = []

    #문자열 검사
    for i in range(len(str)):
        #Empty Stack
        if len(stack) == 0:
            stack.append(str[i])
            continue

        #연속문자 비교
        if stack[-1] == str[i]:
            stack.pop()
        else:
            stack.append(str[i])

    result = len(stack)
    print('#{} {}'.format(test_case, result))