# 1920. 수 찾기

def binary_search(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if target == arr[mid]:
        return 1

    elif arr[mid] > target:
        end = mid
        return binary_search(arr, target, start, end - 1)
    else:
        start = mid
        return binary_search(arr, target, start+1, end)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
target_arr = list(map(int, input().split()))
arr.sort()

for i in range(M):
    result = binary_search(arr, target_arr[i], 0, N-1)
    print(result)