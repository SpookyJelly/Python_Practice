#18352번
# 특정 도시 X로부터 도달할 수 있는 모든 도시 중에서 최단 거리가 정확히 K인거 만 출력
# 모든 도로의 거리는 1
# 가중치가 동일한 다익스트라라고 생각합시다

import sys
sys.stdin = open('18352_input.txt','r')
input = sys.stdin.readline
from heapq import heappop,heappush

def dik(start):
    distance[start] = 0

    heap = []
    heappush(heap,[0,start])


    while heap:

        cur_dis, cur_city = heappop(heap)
        # if not visited[cur_city]: # 이렇게 visited 만들어서 가지치기 할 수도 있는데
        #     visited[cur_city] = True # 안만들어도 가능하구나... 아니 근데 시간은 비슷하네?
        if cur_dis > distance[cur_city]:
            continue
        for dis,next_city in graph[cur_city]:
            new_dis = cur_dis + dis

            if new_dis < distance[next_city]:
                distance[next_city] = new_dis
                heappush(heap,[new_dis,next_city])



N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]
distance = [0xffffff for _ in range(N+1)]
# visited = [False] * (N+1)

for _ in range(M):
    start, goal = map(int,input().split())
    graph[start].append((1,goal))
dik(X)

if distance.count(K):
    for (idx,item) in enumerate(distance):
        if item == K:
            print(idx)

else:
    print(-1)
        

