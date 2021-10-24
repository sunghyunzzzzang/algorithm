# 10828. 스택

"""
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

# N: 명령어 수
N = int(input())
stack = []

for _ in range(N):
    sql = input().split()
    if 'push' == sql[0]:
        stack.append(int(sql[1]))
    elif 'pop' == sql[0]:
        if len(stack) == 0:
            print(-1)
        else:
            pop = stack.pop(-1)
            print(pop)
    elif 'size' == sql[0]:
        print(len(stack))
    elif 'empty' == sql[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' == sql[0]:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
