# 아기 상어


import sys
sys.stdin = open('16236_retry.txt','r')
from collections import deque
import heapq

# 기본 아이디어 : 일단 보이는 물고기 다 먹는다. -> 먹은 물고기 위치, 먹기까지 걸린 시간 모두 저장 -> 먹기까지 가장 오래 걸린 시간 반환 -> 그러기 위해 힙으로 저장

def BFS(lst:list):
    pray = []
    visited = [[False] * N for _ in range(N)]
    queue = deque([lst])

    # 델타 무브 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y,level = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<N and 0<=new_y<N and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                # sea[new_x][new_y] <= shark_size로 퉁치면 안되는 이유 :
                # shark_size보다 작은 물고기들은 먹어야 ( 힙에 넣어야 ) 하기 때문이다.
                if sea[new_x][new_y] == shark_size or sea[new_x][new_y] == 0:
                    queue.append([new_x,new_y,level+1])
                elif sea[new_x][new_y] < shark_size:
                    heapq.heappush(pray,[level+1,new_x,new_y])
    if pray:
        return pray[0]
    else:
        return None


N = int(input())
# 일단 상어 위치 찾아야지

shark_size = 2
fish = []
sea = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            shark = [i,j]
            x,y = i,j
        elif 1<= sea[i][j]<=6:
            fish.append([i,j])

level = 0
count = 0
ate = 0
while fish:
    # 다른 미로문제와는 다르게, 큐가 다 떨어졌어도, 조건에 따라 왔던곳도 다시 이동할 수 있다.
    # 그러니까 다시 방문행렬을 새로 만드는 것
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    result = BFS([x,y,level])
    # result가 있다 --> 뭐라도 잡아왔다
    if result:
        count += result[0]
        x,y = result[1],result[2]
        fish.remove([result[1],result[2]])
        sea[result[1]][result[2]] = 0
        ate += 1
    else:
        break

    if ate >= shark_size:
        shark_size += 1
        ate = 0

print(count)