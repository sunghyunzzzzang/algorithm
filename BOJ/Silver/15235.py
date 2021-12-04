# 15235. Olympiad Pizza

N = int(input())
arr = list(map(int, input().split()))
Max_Time = sum(arr)
result = [0] * len(arr)
T = 1
while 1:
    if T >= Max_Time + 1:
        break
    for i in range(len(arr)):
        # 결과값이 안나왔으면
        if result[i] == 0:
            arr[i] = arr[i] - 1
            # 필요한 만큼 받았으면
            if arr[i] == 0:
                result[i] = T
            T += 1

print(*result)