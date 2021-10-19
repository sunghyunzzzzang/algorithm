# 1932. 정수 삼각형

N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

distance = [[0] * N for i in range(N)]
distance[0][0] = maps[0][0]

for i in range(1, N):
    for j in range(len(maps[i])):
        if j == 0:
            distance[i][j] = maps[i][j] + distance[i-1][j]
        elif i == j:
            distance[i][j] = maps[i][j] + distance[i-1][j-1]
        else:
            distance[i][j] = maps[i][j] + max(distance[i-1][j], distance[i-1][j-1])

print(max(distance[N-1]))