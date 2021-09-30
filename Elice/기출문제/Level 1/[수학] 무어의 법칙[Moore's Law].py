# N : 자연수 N
N = int(input())
result = 1
answer = 0

# 2^N 계산
for i in range(N):
    result *= 2

# 각 자리수 더하기
str_s = str(result)
for i in range(len(str_s)):
    answer += int(str_s[i])

print(answer)