# 1966. 프린터 큐

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    q = []

    for i in range(len(arr)):
        # M번째에 따로 체크해줌
        if M == i:
            q.append((arr[i], 1))
        else:
            q.append((arr[i], 0))

    check = 0
    cnt = 0

    while 1:
        # 중요도가 가장 높으면
        if max(map(max, q)) == q[0][0]:
            temp, check = q.pop(0)
            cnt += 1
        # 중요도가 낮으면
        else:
            temp, temp2 = q.pop(0)
            q.append((temp, temp2))

        if check == 1:
            break

    print(cnt)