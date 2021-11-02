# 2231. 분해합

N = int(input())
i = 0

for i in range(1, 1000001):
    arr = str(i)

    result = i
    # 각 자리수별로 더하기
    for k in range(len(arr)):
        result += int(arr[k])

    if N == result:
        break

if i == 1000000:
    i = 0
print(i)