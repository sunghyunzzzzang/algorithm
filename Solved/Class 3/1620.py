# 1620. 나는야 포켓몬 마스터 이다솜

# N : 포켓몬 개수, M : 문제의 개수
N, M = map(int, input().split())
dict = {}

# 도감 등록
for i in range(1, N+1):
    name = input()
    dict[name] = str(i)
    dict[str(i)] = name

# 문제의 답 출력
for i in range(M):
    print(dict[input()])