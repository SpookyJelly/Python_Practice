#16236번 아기상어
# 시간 제한 2초
import sys
from collections import deque
import heapq
sys.stdin = open('16236_input.txt','r')
# 실제 이동이 필요한가? -> 네

def BFS(s1,s2):
    dq = deque()
    visited = [[False]*N for _ in range(N)]
    heap = []
    dq.append((s1,s2,0)) # 탐색 초기값...초기 위치와 초기위치로부터 현재위치의 거리 넣어준다
    # delta move 상좌하우
    dr = [-1,0,1,0]
    dc = [0,-1,0,1]
    while dq:
        x,y,level = dq.popleft() #bfs니까 0번부터 뽑아야지
        for i in range(4):
            nx = x+dr[i]
            ny = y+dc[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                if sea[nx][ny] == 0 or sea[nx][ny] == size: # 만약에 빈 공간이거나 자기랑 같은 사이즈의 물고기가 있다면
                    # 이동해야하니까 큐에 넣자
                    dq.append((nx,ny,level+1)) # 그리고 여긴 말짱 황이라는 증거로 다음 레벨로 ㄱ
                elif sea[nx][ny] < size: # 내 사이즈보다 작은 놈이면 먹어야지
                    # 힙에 넣자
                    heapq.heappush(heap,[level+1,nx,ny]) # 가장 가까운 새끼 기준으로 정렬해야하니까 level이 제일 앞으로
    if heap:
        return heap[0]
    else:
        return None



N = int(input())
sea = [list(map(int,input().split())) for _ in range(N)]
fish = [] # 바다에 있는 물고기들
size = 2 # 상어 초기 사이즈
cnt = 0 # 정답
ate = 0 # 처먹은 물고기 수
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            s1,s2 = i,j
            sea[i][j] = 0
        elif 1<=sea[i][j]<=6:
            fish.append((i,j))


while fish: # 바다에 물고기가 있는 동안...
    visited = [[False]*N for _ in range(N)]
    visited[s1][s2] = True
    result = BFS(s1,s2) # 처먹은 물고기 있는지 확인

    if result: # 물고기 먹고 왔으면
        cnt += result[0] # level만큼 생존
        ate += 1
        sea[result[1]][result[2]] = 0
    else:
        break
    if ate == size:
        ate = 0
        size += 1

    s1,s2 = result[1],result[2]

print(cnt)