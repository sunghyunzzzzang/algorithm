N = 4
time = 0

for i in range(N):
    time += int(input())

min = time // 60
sec = time % 60

print(min)
print(sec)