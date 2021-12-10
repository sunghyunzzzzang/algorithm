# 8단 변속기

arr = list(map(int, input().split()))
start = arr[0]
result = ''

for i in range(1, len(arr)):
    # 처음 변속순서 정의
    if i == 1:
        if start < arr[i]:
            result = 'ascending'
        else:
            result = 'descending'
    else:
        if result == 'ascending':
            # ascending을 유지하면
            if arr[i-1] < arr[i]:
                continue
            # ascending을 유지못하면
            else:
                result = 'mixed'
                break
        if result == 'descending':
            # descending을 유지하면
            if arr[i-1] > arr[i]:
                continue
            # descending을 유지못하면
            else:
                result = 'mixed'
                break

print(result)