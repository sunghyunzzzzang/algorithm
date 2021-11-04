# 8985. OX퀴즈

N = int(input())
arr = []
for i in range(N):
    arr.append(list(input()))

for i in range(N):
    result = 0
    score = 1
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            result += score
            score += 1
        else:
            score = 1

    print(result)