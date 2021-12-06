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

# 정렬
eat.sort(key = lambda x: (x[2],x[0], x[1]))


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

# 3차원 리스트 넣기
M, N, H = map(int, input().split())
maps = [[] for i in range(H)]

for h in range(H):
    for i in range(N):
        maps[h].append(list(map(int,input().split())))

visited = [[[0] * H for j in range(M)] for i in range(N)]




# 순열 조합

# 주사위 나올 수 있는 모든 경우
# 1 1 1, 1 1 2 ...
def run1(lev):
    if lev == N:
        print(*arr)
        return

    for i in range(1, 7):
        arr.append(i)
        run1(lev+1)
        arr.pop(-1)

# 중복 제외 나올 수 있는 경우
# 1 1 2 == 1 2 1, 2 1 1 (x)
def run2(lev, start):
    if lev >= 3:
        print(*arr)
        return

    for i in range(start, 7):
            arr.append(i)
            run2(lev+1, i)
            arr.pop(-1)
# 모든 다른 수가 나올 수 있는 모든 경우
# 1 2 3 == 1 3 2, 2 1 3 (x)
def run3(lev, num):
    if lev >= 1:
        print(*arr)


    for i in range(num, 7):
        if used[i] == 0:
            used[i] = 1
            arr.append(i)
            run3(lev+1, num)
            arr.pop(-1)
            used[i] = 0
# ???
def run4(lev):
    q = []
    q.append(1)
    while q:
        x = q.pop
        for i in range(x, x+3):
            if used[i] == 0:
                used[i] = 1
                q.append(x)
                used[i] = 0

# 연구소 문제 벽세우기
def wall(x):
    if x == 3:
        print(*maps)
        #bfs()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(x + 1)
                maps[i][j] = 0

n = 3
m = 4
maps = [[1,1,1,1], [0,0,0,0],[1,0,1,0]]
wall(0)

N = 3
M = 2
arr = []
used = [0] * 10

run4(0)
print("########")


# 15650 N과 M (2)

def run(lev, start):
    if lev == M:
        print(*arr)
        return
    for i in range(start, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i)
            run(lev+1, i)
            arr.pop()
            visited[i] = 0


N, M = map(int, input().split())
arr = []
visited = [0] * (N+1)
run(0, 1)

//////////////////////////////////////////////////////