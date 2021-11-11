# 14891. 톱니바퀴


# num : 톱니바퀴 번호, dir : 방향
def rotate(num, dir):
    # 시계방향
    if dir == '1':
        temp = wheel[num][7]
        wheel[num][1:8] = wheel[num][0:7]
        wheel[num][0] = temp
    # 반시계방향
    elif dir == '-1':
        temp = wheel[num][0]
        wheel[num][0:7] = wheel[num][1:8]
        wheel[num][7] = temp

# 1 ~ 4번 사용
wheel = [[]]
for i in range(4):
    wheel.append(list(input()))

# 명령어 개수
command = int(input())
for k in range(command):
    # dir : 1 ~ 4번 사용
    # 2는 초기값
    # '1'이면 시계방향, '-1'이면 반시계방향, 0이면 동작 안함
    dir = [2] * 5

    # start : 톱니바퀴시작번호, d : 방향
    start, d = map(int, input().split())

    # 시작 톱니바퀴에 방향 넣어줌
    dir[start] = str(d)

    # 시작 톱니바퀴 오른쪽 톱니바퀴들 방향 결정
    for i in range(0, 4 - start):
        # 해당 톱니바퀴가 동작 안하면 다음 톱니바퀴도 동작 안함
        if dir[start+i] == 0:
            dir[start + i + 1] = 0
            continue

        # 같은 극이면 동작 안함
        if wheel[start+i][2] == wheel[start+i+1][6]:
            dir[start+i+1] = 0
        # 다른 극이면 반대방향으로 동작
        else:
            if dir[start+i] == '-1':
                dir[start+i+1] = '1'
            else:
                dir[start+i+1] = '-1'

    # 시작 톱니바퀴의 왼쪽 톱니바퀴들 방향 결정
    for i in range(0, start-1):
        # 해당 톱니바퀴가 동작 안하면 다음 톱니바퀴도 동작 안함
        if dir[start-i] == 0:
            dir[start - i - 1] = 0
            continue

        # 같은 극이면 동작 안함
        if wheel[start - i][6] == wheel[start - i - 1][2]:
            dir[start - i - 1] = 0

        # 다른 극이면 반대방향으로 동작
        else:
            if dir[start - i] == '-1':
                dir[start - i - 1] = '1'
            else:
                dir[start - i - 1] = '-1'

    # 톱니 회전
    for i in range(1, 5):
        rotate(i, dir[i])

result = int(wheel[1][0]) + (2*int(wheel[2][0])) + (4*int(wheel[3][0])) + (8*int(wheel[4][0]))
print(result)