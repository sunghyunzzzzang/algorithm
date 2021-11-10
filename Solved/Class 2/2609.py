# 2609. 최대공약수와 최소공배수

A, B = map(int, input().split())

Min = min(A, B)
Max = max(A, B)

#최대공약수
for i in range(Min, 0, -1):
    if A % i == 0 and B % i == 0:
        result1 = i
        break

# 최소공배수
for i in range(Max, A*B+1):
    if i % A == 0 and i % B == 0:
        result2 = i
        break

print(result1)
print(result2)