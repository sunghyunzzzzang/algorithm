# 18405. 경쟁적 전염

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 종류, x, y, 시간을 queue에 넣어줌
def search():
    for i in range(N):
        for j in range(N):
            if maps[i][j] != 0:
                q.append((maps[i][j], i, j, 0))
                visited[i][j] = 1

def bfs():

    while q:
        virus, x, y, time = q.pop(0)
        # 주어진 시간이 다 되면
        if time == S:
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not nx in range(N) or not ny in range(N):
                continue
            if visited[nx][ny] != 0:
                continue

            visited[nx][ny] = 1
            maps[nx][ny] = virus
            q.append((virus, nx, ny, time + 1))


# N: 배열 크기, K: 바이러스 종류 개수
N, K = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

S, x_end, y_end = map(int, input().split())

visited = [[0] * N for i in range(N)]

q = []

# 바이러스 종류, x, y, 시간을 queue에 넣어줌
search()
# 바이러스 종류의 숫자가 낮을수록 우선순위
q.sort()

bfs()

result = maps[x_end-1][y_end-1]
print(result)