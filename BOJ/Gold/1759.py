# 1759. 암호 만들기

dict = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0
}


def run(lev):
    global moeum, jaeum
    # 알파벳이 증가하는 순서가 아닐 때
    if lev >= 2:
        if ord(str[lev-2]) >= ord(str[lev-1]):
            return

    # L자리 문자열 일 때
    if lev == L:
        # 모음이 한 개 그리고 자음이 두 개 이상일 때
        if moeum >= 1 and jaeum >= 2:
            print("".join(str))
        return

    for i in range(C):
        if used[i] == 0:
            # 모음 자음 체크, 사용한 문자인지 체크
            if arr[i] in dict:
                moeum += 1
            else:
                jaeum += 1
            used[i] = 1
            str.append(arr[i])

            run(lev+1)

            # 재귀를 나오면서 다시 '-' 를 해줌
            if arr[i] in dict:
                moeum -= 1
            else:
                jaeum -= 1
            used[i] = 0
            str.pop()



L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

str = []
used = [0] * C
moeum = 0
jaeum = 0

run(0)