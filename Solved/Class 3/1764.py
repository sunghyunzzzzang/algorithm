# 1764. 듣보잡

N, M = map(int, input().split())
dict = {}
result = []
cnt = 0

for i in range(N):
    dict[input()] = 0

for i in range(M):
    str = input()
    if str in dict:
        result.append(str)
        cnt += 1

result.sort()
print(cnt)
for i in result:
    print(i)