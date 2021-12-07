# 지도 자동 구축

import math

N = int(input())
arr = [4, 9, 25]
if N == 0:
    answer = arr[0]
elif N == 1:
    answer = arr[1]
elif N == 2:
    answer = arr[2]
else:
    for i in range(3, N+1):
        # 다음 변의 점의 개수 = 한 변의 점의 개수 - 1 개 만큼 증가
        add = 2 * math.sqrt(arr[i-1]) - 1
        result = add*add
        arr.append(result)

print(int(arr[N]))