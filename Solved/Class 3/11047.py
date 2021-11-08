# 11047. 동전 0

N, K = map(int, input().split())
coin = []
result = 0
for i in range(N):
    coin.append(int(input()))

# 동전 종류를 내림차순으로 변경
coin.reverse()

for i in range(len(coin)):
    # K가 동전 종류보다 크거나 같으면
    if K >= coin[i]:
        result += K // coin[i]
        K = K % coin[i]

    # K원이 0이 되면 종료
    if K == 0:
        break

print(result)