#1261번
# 설명 생략 : 옛날에 보급로 문제랑 비슷함

# 기본 맥락은 다 똑같았는데 시간초과, 메모리 초과 나옴 <-- 큐가 터져버리는 문제이다.
# 이걸 deque를 힙으로 바꾸고, 방문 체크를 도입해서 벽 부수는 움직임이 0쪽으로 우선해서 가는걸로 한다. 그러면 방문 체크도 되고 일석이조
import sys
sys.stdin = open('1261_input.txt','r')

from heapq import heappop,heappush
input = sys.stdin.readline
N, M = map(int,input().split())

inf = 0xfffffff

maze = [list(input()) for _ in range(M)]
visited = [[False]*N for _ in range(M)]


# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def make_path():

    heap = []
    heappush(heap,[0,0,0])
    while heap:
        wall_cnt,x,y = heappop(heap)

        if (x,y) == (M-1,N-1):
            print(wall_cnt)

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                if maze[nx][ny] == '1':
                    heappush(heap,[wall_cnt+1,nx,ny])
                else:
                    heappush(heap,[wall_cnt,nx,ny])
                visited[nx][ny] = True
make_path()