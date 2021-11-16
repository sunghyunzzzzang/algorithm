# 17219. 비밀번호 찾기

# N : 저장된 사이트 주소의 수, M : 비밀번호를 찾으려는 사이트 주소의 수
N, M = map(int, input().split())

dict = {}

# 비밀번호 저장
for i in range(N):
    site, password = map(str, input().split())
    dict[site] = password

# 비밀번호 찾기
for j in range(M):
    search_site = input()
    print(dict[search_site])