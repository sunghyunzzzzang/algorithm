# 5430. AC

from collections import deque

TC = int(input())
for test_case in range(1, TC+1):
    command = input()
    N = int(input())
    str = input()

    if len(str) == 2:
        temp = []
    else:
        temp = list((str[1:-1].split(",")))
    arr = deque(temp)

    check = 1
    dir = 1

    for i in range(len(command)):
        # 'R' 일 때
        if command[i] == 'R':
            dir *= -1
        # 'D' 일 때
        elif command[i] == 'D':
            # error
            if len(arr) == 0:
                check = 0
                break

            # 앞에서 버리기
            if dir == 1:
                arr.popleft()
            # 뒤에서 버리기
            else:
                arr.pop()


    if dir == -1:
        arr.reverse()
    # 출력
    if check:
        print('[', end="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i == len(arr)-1:
                break
            print(',', end="")
        print(']')

    else:
        print('error')