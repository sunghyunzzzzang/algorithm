# 14503. 로봇 청소기
# solved
# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def run(x, y, direction):
    cnt = 0
    clean = [[0] * M for i in range(N)]

    while 1:
        # 현재 자리 청소
        clean[x][y] = 1
        for d in range(4):
            cnt += 1
            # 좌회전
            direction = (direction + 3) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            if not nx in range(N) or not ny in range(M):
                continue
            # 빈 칸이고, 청소하지 않은 공간이면,
            if maps[nx][ny] == 0 and clean[nx][ny] == 0:
                # 위치 방향 저장
                x = nx
                y = ny
                cnt = 0
                break
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
        if cnt == 4:
            back = (direction + 2) % 4
            nx = x + dx[back]
            ny = y + dy[back]
            # 후진
            if nx in range(N) and ny in range(M) and maps[nx][ny] == 0:
                # 위치 방향 저장
                x = nx
                y = ny
                cnt = 0
            # 동작 멈춤
            else:
                return sum(map(sum, clean))


N, M = map(int, input().split())
r, c, direction = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

result = run(r, c, direction)

print(result)