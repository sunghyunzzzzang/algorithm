# 11726. 2xN 타일링

N = int(input())
arr = []
arr.append(0)
arr.append(1)
arr.append(2)

for i in range(3, N+1):
    Num = (arr[i-1] + arr[i-2]) % 10007
    arr.append(Num)

print(arr[N])