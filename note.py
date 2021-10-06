https://freedeveloper.tistory.com/365

#숫자 리스트 -> 문자열로
_str = []
    _str = "".join(map(str, arr))
    print(_str)


#Array(ex. 2차원 배열)에서 max값만 추출하는 방법
numbers = [0, 0, 1, 0, 0, 1], [0, 1, 0, 2, 0, 0], [0, 0, 2, 0, 0, 1], [0, 1, 0, 3, 0, 0], [0, 0, 0, 0, 4, 0]

>>> list(map(max, numbers))
[1, 2, 2, 3, 4]

>>> max(map(max, numbers))
4

#2차원 배열 받을 때 (NO Split)
# input
"""
5
13101
10101
10101
10101
10021
"""
# 방법 1
N = int(input())
maze = [list(map(int, list(input()))) for _ in range(N)]

# 방법 2
N = int(input())
maze = []

for i in range(N):
    maze.append(list(map(int, list(input()))))

# 방법 3
maze = [[0] * N for i in range(N)]
for i in range(N):
    maze[i] = list(map(int, input()))


#2차원 배열 0으로 초기화
visited = [[0] * N for i in range(N)]


# 사방탐색
if nx in range(N) and ny in range(N):
    stack.append((nx, ny))
    visited[nx][ny] = 1
else:
    continue


# 문자열 뒤집기
print(int(Cat_N[::-1]) + int(elice_N[::-1]))

#정렬
student_tuples = [
    ['john', 'A', 15],
    ['jane', 'B', 12],
    ['dave', 'B', 10],
]
result = sorted(student_tuples, key=lambda st: st[2])
print(result)

# hash
for _ in range(M):
	s, e = map(int,input().split())
	snake[s] = e

# 부분조합
from itertools import combinations
from itertools import permutations

N = int(input())
arr = []
result = 0
for i in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

max_len_arr = max(map(max,arr))
print(max_len_arr)
time = [0 for i in range(max_len_arr)]

comb = []

arr.sort()

print(arr)
for k in range(1, len(arr)+1):
    c = permutations(arr, k)
    comb.extend(c)
    print(comb)

    for index in range(len(comb)):
        start, end = comb[index]
        for j in range(start, end):
            if time[j] == 1:
                break
            time[j] += 1
            result += 1
        time = [0 for i in range(max_len_arr)]

print(result)