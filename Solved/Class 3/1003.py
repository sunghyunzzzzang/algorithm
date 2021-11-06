# 1003. 피보나치 함수

T = int(input())
for tc in range(1, T + 1):
    count = [0] * 2
    N = int(input())

    arr = []
    arr.append((1,0))
    arr.append((0,1))

    for i in range(2, N+1):
        a1, b1 = arr[i-2]
        a2, b2 = arr[i-1]
        arr.append((a1+a2, b1+b2))

    print(arr[N][0], arr[N][1])