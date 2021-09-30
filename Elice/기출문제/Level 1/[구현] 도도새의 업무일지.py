N = int(input())

arr = list(map(int, input().split()))
result = []

result.append(arr[0])

for i in range(1,N):
    result.append((arr[i] * (i+1)) - sum(result))

for i in result:
    print(i, end=' ')
