blue_team = list(map(int, input().split()))
white_team = list(map(int, input().split()))
sum_blue = 0
sum_white = 0

for i in range(len(blue_team)):
    sum_blue += blue_team[i]
    sum_white += white_team[i]

print(max(sum_blue, sum_white))