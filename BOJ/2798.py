# 2798. 블랙잭

# N: 카드 수, M: 3장의 카드의 숫자를 합친 목표
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
Max = 0


for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = arr[i] + arr[j] + arr[k]
            if sum <= M:
                result = max(sum, result)

print(result)
