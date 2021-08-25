#4869. 종이붙이기
# 계산식
# a[2] = (a[0] * 2) + a[1]
# 재귀
import sys
sys.stdin = open("input.txt", "r")

def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (paper(n-2) * 2) + paper(n-1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = paper(N/10)
    print('{} {}'.format(result))