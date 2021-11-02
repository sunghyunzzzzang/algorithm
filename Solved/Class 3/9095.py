# 9095. 1, 2, 3 더하기
# Solved
# DP

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    arr = [0] * 12
    arr[0] = 0
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4

    for i in range(4, n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    print(arr[n])