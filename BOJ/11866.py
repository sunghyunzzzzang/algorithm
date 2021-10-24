# 11866. 요세푸스 문제 0

# N: N번, K: K번째 수
N, K = map(int, input().split())
q = []
clear = []
for i in range(1, N+1):
    q.append(i)


# K가 3이면 배열 index는 2번째여서 -1 해줌
index = -1
for i in range(1, N+1):
    cnt = 0
    # K번째 수 뽑아내기
    while cnt < K:
        # 배열 최대크기를 넘어가지 않게 설정
        index = (index + 1) % N
        # 배열값이 0 이면 카운트 하지 않음
        if q[index] == 0:
            continue
        cnt += 1
    # K번째 수 clear에 저장 한 후 0을 넣어줌
    num = q[index]
    clear.append(num)
    q[index] = 0

print('<', end="")
for i in range(N-1):
    print("{}, ".format(clear[i]), end="")
print(clear[N-1], end="")
print('>')