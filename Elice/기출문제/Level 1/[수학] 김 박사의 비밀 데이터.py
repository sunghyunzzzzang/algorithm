# N : 저장할 데이터의 개수
N = int(input())
arr = []
str_s = []
result = 0


for i in range(N):
    result += int(input())

answer = str(result)
print(answer[0:10])