# 2798. 블랙잭

from itertools import combinations

# N: 카드 수, M: 3장의 카드의 숫자를 합친 목표
N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in combinations(arr, 3):
    if sum(i) <= M:
        result = max(sum(i), result)

print(result)