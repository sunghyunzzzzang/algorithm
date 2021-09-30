# N : 총 상품의 개수, S : 최소 금액
N, S = map(int, input().split())
# 상품의 가격
arr = list(map(int, input().split()))

answer = []

# cnt : 개수, sum : 상품의 가격 합
cnt = 0
sum = 0
j = 0

# 상품의 개수만큼 반복
for i in range(len(arr)):
    # i번째 기준으로 j를 움직여 구간 합 구하기
    while i + j < len(arr):
        # 최소 금액을 넘으면 break
        if sum >= S:
            answer.append(cnt)
            break

        sum += arr[j]
        cnt += 1
        j += 1

    sum = 0
    j = i
    cnt = 0

# 최소 금액 쇼핑이 불가능 하면
if len(answer) == 0:
    print(0)
# 최소 개수 출력
else:
    print(min(answer))