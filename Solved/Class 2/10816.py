# 10816. 숫자 카드 2

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
dict = {}
result = []

for i in range(N):
    if arr[i] in dict:
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

for i in range(M):
    if arr2[i] in dict:
        result.append(dict[arr2[i]])
    else:
        result.append(0)

print(*result)