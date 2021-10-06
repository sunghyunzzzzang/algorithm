# 1931. 회의실배정

# N : 회의의 개수, last: 마지막 회의 시간
N = int(input())
arr = []
result = 0
last = 0

for i in range(N):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key=lambda x : x[0])
arr = sorted(arr, key=lambda x : x[1])

for i in range(N):
    start, end = arr[i][0], arr[i][1]
    if start >= last:
        result += 1
        last = end

print(result)