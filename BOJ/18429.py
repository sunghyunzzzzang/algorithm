# 18429. 근손실

def run(lev, weight):
    global result
    # 중량이 500보다 낮아지면
    if weight < 500:
        return
    # 운동 키트 적용 순서 조건 만족하면
    if lev == N:
        result += 1
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            run(lev+1, weight+num[i]-K)
            used[i] = 0

# N: N일, N개의 운동키트, K: 하루 지나면 감소하는 중량
N, K = map(int, input().split())
num = list(map(int, input().split()))
used = [0] * N

weight = 500
result = 0
run(0, weight)

print(result)