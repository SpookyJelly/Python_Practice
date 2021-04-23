# 4485번 젤다

import sys
sys.stdin = open('4485_input.txt','r')
from collections import deque

cnt = 0
while True:
    cnt+=1
    N = int(input())
    if N == 0:
        break
    lst = [list(map(int,input().split())) for _ in range(N)]
    # print(lst)
    D = [[0xfffff] * N for _ in range(N)]
    D[0][0] = lst[0][0]

    def BFS(x,y):
        que = deque([[x,y]])
        # 델타 무브 상하좌우
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while que:
            x,y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx <N and 0<= ny <N:
                    weight =  lst[nx][ny]
                    if D[x][y]+weight < D[nx][ny]:
                        D[nx][ny] = D[x][y]+weight
                        que.append([nx,ny])
    BFS(0,0)
    # print(D)
    print('Problem {0}: {1}'.format(cnt,D[N-1][N-1]))