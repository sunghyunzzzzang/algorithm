# 9012. 괄호

# T: Test_case
T = int(input())
for i in range(1, T+1):
    #괄호 입력
    str = input()
    stack = []

    stack.append(str[0])
    for i in range(1, len(str)):
        # ')'만 있을 때 break
        if len(stack) == 1 and stack[-1] == ')':
            break

        # stack이 비어있지 않을 때
        if len(stack) != 0:
            # top이 '('고  ')' 가 들어가야 할 때
            if stack[-1] == '(' and str[i] == ')':
                stack.pop()
            # top이 '('가 아닐 때
            else:
                stack.append(str[i])
        # stack이 비어있을 때
        else:
            stack.append(str[i])


    if len(stack):
        print('NO')
    else:
        print('YES')