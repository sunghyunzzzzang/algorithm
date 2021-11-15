# 1987. 알파벳

dict = {
    'A' : 0,
    'B' : 0,
    'C' : 0,
    'D' : 0,
    'E' : 0,
    'F' : 0,
    'G' : 0,
    'H' : 0,
    'I' : 0,
    'J' : 0,
    'K' : 0,
    'L' : 0,
    'M' : 0,
    'N' : 0,
    'O' : 0,
    'P' : 0,
    'Q' : 0,
    'R' : 0,
    'S' : 0,
    'T' : 0,
    'U' : 0,
    'V' : 0,
    'W' : 0,
    'X' : 0,
    'Y' : 0,
    'Z' : 0,
}

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, result):
    global answer

    # 최대값 저장
    if result > answer:
        answer = result

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        # 배열 크기 체크
        if nx not in range(N) or ny not in range(M):
            continue
        # 방문 체크
        if visited[nx][ny] != 0:
            continue
        # 새로운 알파벳이면
        if dict[maps[nx][ny]] == 0:
            dict[maps[nx][ny]] = 1
            visited[nx][ny] = 1
            dfs(nx, ny, result + 1)
            visited[nx][ny] = 0
            dict[maps[nx][ny]] = 0

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(input())

visited = [[0] * M for i in range(N)]
answer = 0

visited[0][0] = 1
dict[maps[0][0]] = 1
dfs(0, 0, 1)

print(answer)