#1916번

# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

import sys
sys.stdin = open('1916_input.txt','r')

from heapq import heappush, heappop

input = sys.stdin.readline

def dik (start):
    heap = []
    heappush(heap,[0,start])
    while heap:
        w, n = heappop(heap)
        if distance[n] < w:
            continue
        for nex_city, wei in graph[n]:
            new_w = w + wei
            if distance[nex_city] > new_w:
                distance[nex_city] = new_w
                heappush(heap,[new_w,nex_city])

# 이건 모든 버텍스를 조사하니까 (1이 닿지 않는 곳도) <-- 당근 느리겠다
# def dik ():

#     for idx in range(1,N):
#         que = graph[idx]
#         heapq.heapify(que)
#         # current_city = idx
#         while que:
#             close_city,weight= heapq.heappop(que)
#             if not visited[idx] and distance[close_city] > distance[idx] + weight:
#                 distance[close_city] = distance[idx] + weight


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [100000000] * (N+1)

for idx in range(M):
    start,goal,weight =map(int,input().split())
    graph[start].append((goal,weight))

start_city, goal_city = map(int,input().split())
# print(graph)
distance[start_city] = 0
dik(start_city)
# print(distance)
print(distance[goal_city])
