#5432. 쇠막대기 자르기
#Stack 사용
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = 0
    str = input()
    stack = []
    i = 0

    while i < len(str):
        # '('  일때
        if str[i] == '(':
            # '()' 레이저일때 Stack에 쌓인 쇠막대기 개수만큼 증가
            if str[i+1] == ')':
                result = result + len(stack)
                i += 1
            # 쇠막대기 추가 stack에 '(' 추가
            else:
                stack.append(str[i])
        # ')' 일때 stack pop 실행
        elif str[i] == ')':
            stack.pop()
            result += 1
        i += 1

    print('#{} {}'.format(test_case, result))