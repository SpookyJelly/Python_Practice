# 1753번 최단경로
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오.
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다.

# 입력 

# (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다.
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다.
# u와 v는 서로 다르며 w는 10 이하의 자연수이다.
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

#출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

import sys
import heapq
sys.stdin = open('1753_input.txt','r')

# key 1 :시간을 줄이기 위해서 input 보다 더 빠른 입력, readline()을 사용했다 
V,E = map(int,sys.stdin.readline().split()) #  정점의 갯수 V , 간선의 개수 E 
K = int(input()) # 시작 정점의 번호

# key 2 : 인접 행렬로도 그래프를 그릴 수 있는데, 그러면 공간 복잡도가 O(N^2) 이 되어서 메모리 초과가 난다.
graph = [[] for _ in range(V+1)]

INF = float('inf') 

# 초기값 셋팅
distance = [INF] * (V+1) # 노드별 거리 초기화
distance[K] = 0 # 시작노드 거리 초기화


# 그래프 그리기 : 어짜피 heapq를 이용하여 거리 순으로 자동 오름차순 정렬 할 것이기 때문에
# 입력 받으면서 출발/도착 노드가 같은 경우의 최소 가중치를 계산하여 넣을 필요가 없다.
for _ in range(E):
    u,v,e = map(int,sys.stdin.readline().split())
    graph[u].append((v,e))


# key 3: 방문 체크를 시행하여, 이미 최소값이 나온 노드에 대해서는 다익스트라를 수행하지 않는다 
# heapq를 이용하기 때문에 while heap이 끝나는 그 시점에서 해당 노드를 방문하는 최소 거리가 보장된다.
visited = [False] * (V+1)
heap = []
heapq.heappush(heap,(0,K)) # K번 노드로부터 모험을 떠나므로, 거리가 0인 상태로 시작한다

while heap:
    min_dis, cur_node = heapq.heappop(heap)
    
    # 현재 경로를 탐색할 노드가 이미 방문한 적이 있는 노드라면 스킵한다.
    if visited[cur_node]:
        continue
    # 방문 한 적이 없는 노드라면, 방문 처리를 해준다.

    visited[cur_node] = True

    # 현재 노드와 연결된 모든 노드와 거리를 대상으로 이하의 검사를 시행한다.
    for node,dis in graph[cur_node]:
        # 1. new_d 는 현재 노드까지 오기 까지의 거리 min_dis와 현재 노드에서 node까지의 거리인 dis의 합이다.
        new_d = min_dis+dis

        # 2.만약에 이렇게 계산한 거리가 기 저장되어있었던 거리보다 작다면, 값을 바꿔준 다음, heap에 새로운 값을 투입해준다.
        # (더 탐색할 가치가 있다는 뜻으로 넣어주는 것이다.)
        if new_d < distance[node]:
            distance[node] = new_d
            heapq.heappush(heap,(new_d,node))

# 문제의 출력 형식에 맞추어 출력
for idx in range(1,len(distance)):
    if distance[idx] == INF:
        print('INF')
    else:
        print(distance[idx])

