# 4153. 직각삼각형

while 1:
    arr = list(map(int, input().split()))

    # 종료 조건
    if sum(arr) == 0:
        break

    arr.sort()
    # 피타고라스 정리
    if (arr[0]**2) + (arr[1]**2) == arr[2]**2:
        print('right')
    else:
        print('wrong')