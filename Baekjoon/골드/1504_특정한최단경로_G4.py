#1504번 특정한 최단 경로
# 다익스트라는 프림과 다르게, 일단 노드에서 뻗어있는 간선들을 전부 비교해보긴 한다.
# 원래는 방문체크도 해줘야하는데, 이번 문제 특징상 안했다

import sys
sys.stdin = open('1504_input.txt','r')
import heapq
input = sys.stdin.readline

def dik(start):
    node_weight = [sys.maxsize] * (N+1)
    node_weight[start] = 0

    heap = []
    heapq.heappush(heap,[0,start])

    while heap:
        # weight = 가중치 , cur_vtx = 현 위치
        weight,cur_vtx = heapq.heappop(heap)
        for nw, nv in graph[cur_vtx]:
            ad_weight = weight + nw
            if ad_weight < node_weight[nv]:
                node_weight[nv] = ad_weight
                heapq.heappush(heap,[node_weight[nv],nv])
    return node_weight



N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1, v2 = map(int,input().split())

from_start = dik(1)
v1_start = dik(v1)
v2_start = dik(v2)
routeA = from_start[v1] + v1_start[v2] + v2_start[N]
routeB = from_start[v2] + v2_start[v1] + v1_start[N]
ans = min(routeA,routeB)
print(ans if ans < sys.maxsize else -1)