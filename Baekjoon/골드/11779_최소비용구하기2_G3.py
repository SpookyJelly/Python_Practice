# 11779번 최소비용 구하기 2

import sys
import heapq
sys.stdin = open('11779_input.txt','r')
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
node_weight_path = [[sys.maxsize,[]] for _ in range(n+1)]
for _ in range(m):
    depart_city_num,arrival_city_num,cost = map(int,input().split())
    graph[depart_city_num].append((arrival_city_num,cost))

start_city, goal_city = map(int,input().split())


node_weight_path[start_city][0] = 0
node_weight_path[start_city][1] = [start_city]

def dik(start):
    heap = []
    heapq.heappush(heap,[0,start_city])

    while heap:
        cur_weight, cur_city = heapq.heappop(heap)

        # # 더 볼 필요 없으면 패스
        if cur_weight > node_weight_path[cur_city][0]:
            continue

        for nxt_city , nxt_cost in graph[cur_city]:
            if nxt_cost + cur_weight < node_weight_path[nxt_city][0]:
                node_weight_path[nxt_city][0] = cur_weight + nxt_cost
                node_weight_path[nxt_city][1] = node_weight_path[cur_city][1] + [nxt_city]
                heapq.heappush(heap,[nxt_cost + cur_weight,nxt_city])

dik(start_city)

print(node_weight_path[goal_city][0])
print(len(node_weight_path[goal_city][1]))
print(*node_weight_path[goal_city][1])
