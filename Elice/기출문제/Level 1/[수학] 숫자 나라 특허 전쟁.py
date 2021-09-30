N = int(input())
result = 0

for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)