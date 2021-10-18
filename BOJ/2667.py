# 2667. 단지번호붙이기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = []
    q.append((x, y))
    maps[x][y] = 0
    cnt = 1

    while q:
        x, y = q.pop(0)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 범위 체크
            if not nx in range(N) or not ny in range(N):
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                continue
            # 집 체크
            if maps[nx][ny] == 0:
                continue
            # 방문한 집을 없애줌
            maps[nx][ny] = 0
            visited[nx][ny] = 1
            q.append((nx, ny))
            # 집 개수
            cnt += 1
    return cnt

# 배열 크기 N*N
N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, list(input()))))

visited = [[0] * N for i in range(N)]
answer = []
count = 0

# maps에서 1인 좌표값 찾기
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            result = bfs(i, j)
            answer.append(result)
            count += 1

# 출력
print(count)
answer.sort()
for i in range(len(answer)):
    print(answer[i])