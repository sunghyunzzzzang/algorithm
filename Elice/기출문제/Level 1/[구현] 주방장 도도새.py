# N : 주문수, time : 근무시간
N, time = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(len(arr)):
    time -= arr[i]
    if time <= 0:
        break
    result += 1

print(result)