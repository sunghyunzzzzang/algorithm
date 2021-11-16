# 18870. 좌표 압축

N = int(input())
arr = list(map(int, input().split()))
temp = sorted(arr)
dict = {}
cnt = 0
result = []

for i in range(N):
    if temp[i] in dict:
        continue
    else:
        dict[temp[i]] = cnt
    cnt += 1

for i in range(N):
    result.append(dict[arr[i]])

print(*result)