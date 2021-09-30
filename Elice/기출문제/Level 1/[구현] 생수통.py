N = 3
M = 2

bottle_arr = []
cover_arr = []

for i in range(N):
    bottle_arr.append(int(input()))
for i in range(M):
    cover_arr.append(int(input()))

sum = min(bottle_arr) + min(cover_arr) + 10

print(sum)