import math

# 높이 = 올림(올라가는 높이 - 내려가는 높이)x + 올라가는 높이
# V = 올림(A-B)x + A
# x = 올림(V-A)/(A-B)
# answer = x + 1

# x = 올림(5-2)/(2-1)
# answer = 3 + 1

A, B, V = map(int, input().split())

x = math.ceil((V-A)/(A-B))
answer = x + 1

print(answer)