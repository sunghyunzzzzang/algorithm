# 2947. 나무 조각

arr = list(map(int, input().split()))
goal = sorted(arr)

while 1:
    if arr == goal:
        break
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)