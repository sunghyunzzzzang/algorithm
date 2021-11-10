# 1547. 공

N = int(input())
# 1 ~ 3번 컵 사용
arr = [0] * 4
# 첫번째 컵에 공 넣기
arr[1] = 1

# 자리 바꿈
for i in range(N):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]

# 공 들어가있는 컵 출력
for i in range(len(arr)):
    if arr[i] == 1:
        print(i)
        break