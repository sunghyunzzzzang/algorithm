# 2292 벌집
"""
1 7 19 37
 6 12 18
  6  6
"""

#N : 숫자, i: 방 개수
N = int(input())
i = 0
_sum = 0

# 맨 처음 값
_sum = 1
i += 1
# N 값이 넘어갈 때 까지
while N >= _sum:
    if N == _sum:
        break
    _sum += i*6
    i += 1

print(i)