# 10814. 나이순 정렬

N = int(input())
arr = []
for i in range(N):
    arr.append(list(input().split()))

arr = sorted(arr, key = lambda st : int(st[0]))

for i in range(N):
    #print(*arr[i])                 # 출력 형식 1
    print(arr[i][0], arr[i][1])     # 출력 형식 2