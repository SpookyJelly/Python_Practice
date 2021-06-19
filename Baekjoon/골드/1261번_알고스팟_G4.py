#1261번
# 설명 생략 : 옛날에 보급로 문제랑 비슷함

# 기본 맥락은 다 똑같았는데 시간초과, 메모리 초과 나옴 <-- 큐가 터져버리는 문제이다.
# 이걸 deque를 힙으로 바꾸고, 방문 체크를 도입해서 벽 부수는 움직임이 0쪽으로 우선해서 가는걸로 한다. 그러면 방문 체크도 되고 일석이조
import sys
sys.stdin = open('1261_input.txt','r')
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())

inf = 0xfffffff

min_wall = [[inf]*N for _ in range(M)]
maze = [list(input()) for _ in range(M)]
min_wall[0][0] = 0


# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_path():

    que = deque()
    que.append([0,0,0]) # 초기화

    while que:
        x,y,wall_cnt = que.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            # if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
            if 0<=nx<M and 0<=ny<N and min_wall[nx][ny] > wall_cnt:
                # visited[nx][ny] = True
                if maze[nx][ny] == '1':
                    # maze[nx][ny] = '0'
                    min_wall[nx][ny] = wall_cnt+1
                    # que.append([nx,ny,min(wall_cnt+1,min_wall[nx][ny])])
                    que.append([nx,ny,wall_cnt+1])
                else:
                    min_wall[nx][ny] = wall_cnt
                    # que.append([nx,ny,min(wall_cnt,min_wall[nx][ny])])
                    que.append([nx,ny,min_wall[nx][ny]])

make_path()
print(min_wall[M-1][N-1])