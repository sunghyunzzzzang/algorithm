# N : 물건의 값
N = int(input())
# arr : 지폐 종류
arr = [10000, 1000, 100, 10, 1]
answer = 0

# 거스름돈 계산
result = 10000 - N

# 몫, 나머지 계산
for i in range(len(arr)):
    answer += result // arr[i]
    result = result % arr[i]

print(answer)