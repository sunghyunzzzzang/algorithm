# 1987. 알파벳

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
        index = ord(maps[nx][ny]) - ord('A')
        if dict[index] == 0:
            dict[index] = 1
            visited[nx][ny] = 1
            dfs(nx, ny, result + 1)
            visited[nx][ny] = 0
            dict[index] = 0

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(input())

visited = [[0] * M for i in range(N)]
dict = [0] * 26
answer = 0

visited[0][0] = 1
dict[ord(maps[0][0]) - ord('A')] = 1
dfs(0, 0, 1)

print(answer)