# 1676. 팩토리얼 0의 개수

# 팩토리얼 구하기
def sol(N):
    global result
    if N == 0:
        return
    else:
        result = result * N
        sol(N-1)
    return

result = 1

sol(int(input()))

# 문자열 변경 후 reverse
result = str(result)
result = result[::-1]

answer = 0
# 0의 개수 구하기
for i in range(len(result)):
    if result[i] == '0':
        answer += 1
    else:
        break

print(answer)