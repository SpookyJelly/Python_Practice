#16236번 아기상어
# 시간 제한 2초
import sys
from collections import deque
sys.stdin = open('16236_input.txt','r')
# 실제 이동이 필요한가?

def BFS(start:tuple):
    dq = deque()

    # delta move 상좌하우
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]




N = int(input())
sea = []
for idx in range(N):
    tem = list(map(int,input().split()))
    if 9 in tem:
        start = (idx,tem.index(9))
    sea.append(tem)

print(sea)
print(start)

# 상어 처음 크기
shark = 2