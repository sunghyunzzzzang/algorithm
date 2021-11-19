# 1920. 수 찾기

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dict = {}
for i in range(N):
    temp = arr1.pop()
    dict[temp] = 1

for i in range(M):
    if arr2[i] in dict:
        print(1)
    else:
        print(0)