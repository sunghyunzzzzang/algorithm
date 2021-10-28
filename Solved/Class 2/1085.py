# 1085. 직사각형에서 탈출

x, y, w, h = map(int ,input().split())

"""
 (0,0)에서 (x,y)거리
 (h,y)에서 (x,y)거리
 최소값 출력
"""
print(min(x, y, w-x, h-y))