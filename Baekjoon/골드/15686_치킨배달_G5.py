# #15686 치킨배달
# 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 
# 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
# 이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 
# 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 
# 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.



# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
# 도시의 정보는 0, 1, 2로 이루어져 있고, 
# 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 
# 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

import sys
sys.stdin = open('15686_input.txt','r')
from pprint import pprint
from itertools import combinations
from collections import deque

# 기본 아이디어.. 표본 수가 적으니까 브루트 포스 이용해도 된다.
# 일단 치킨집이 M개 남을때까지 다 지워보는 것이다.
# 정확히 말하자면, 치킨집 목록에서 치킨집이 M 개 남은 조합을 만들어서, 그 각 조합에 대해 치킨거리를 구하면 된다. -> itertools 이용
# 치킨거리는 BFS로 이용하면 되지 않을까?
# 그 전에 인풋에 한줄/ 한열 씩 추가해줘서 인덱스를 0부터 활용할 수 있게 하자.
N,M = map(int,input().split())
KFC = [] # 치킨 집의 위치
home = [] # 도시에 있는 집 위치

for i in range(1,N+1):
    city_block = list(map(int,input().split()))
    for j in range(N):
        if city_block[j] == 1:
            home.append([i,j+1])
        elif city_block[j] == 2:
            KFC.append([i,j+1])


# combinations는 한번 쓰고 방출된다고 하네...
survivor = combinations(KFC,M)

new_city = [[0]*(N+1) for _ in range(N+1)]
for h in home :
    home_x = h[0]
    home_y = h[1]
    new_city[home_x][home_y] = 1

# 이제 여기서부터 살아남은 닭집 하나씩 집어넣고, BFS 돌리면 된다.
# 여기서 BFS 돌린다.

def BFS(copyed_home:list,new_city:list,min_dis:int):

    # 일단 각 집에서 치킨집 가는거 구현 deque 가져와라

    # 델타 무브 / 상하좌우
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    chicken_dis = 0
    while copyed_home:
        # 방문처리 구현...이거 왜 맨날 까먹을까
        visited = [[False]*(N+1) for _ in range(N+1) ]
        if min_dis >= chicken_dis: # 이건 최고 기록보다 넘었는지 확인하는 함수 아직 안넘었으면 (TRUE) -> 계속 진행 -> 아니면 종료 (False)
            # 큐 초기화
            que = deque()
            que.append(copyed_home.pop())
            [init_x,init_y] = que[0]
            flag = False
            while que:
                x,y = que.popleft()
                for i in range(4):
                    new_x = x+dx[i]
                    new_y = y+dy[i]
                    # 인풋이 희안하게 들어와서 범위체크 방식도 좀 다르다.
                    if 1<=new_x<=N and 1<=new_y<=N and not visited[new_x][new_y]:
                        if new_city[new_x][new_y] == 2:
                            chicken_dis += abs(new_x-init_x) + abs(new_y-init_y)
                            flag = True
                            break
                        else:
                            que.append([new_x,new_y])
                            visited[new_x][new_y] = True
                if flag:
                    break
        else:
            return 0xfffff
    
    # 순회 끝나고, 여기서 최소 거리 경신함
    return chicken_dis

min_dis = 0xffffff
result = 0
for s in survivor:
    clean_it =[]
    copyed_home = home[:]
    for market in s:
        KFC_x = market[0]
        KFC_y = market[1]
        new_city[KFC_x][KFC_y] = 2
        clean_it.append([KFC_x,KFC_y])
    result= BFS(copyed_home,new_city,min_dis)
    for elem in clean_it:
        new_city[elem[0]][elem[1]] = 0
    if result < min_dis:
        min_dis = result


print(min_dis)
# 시간 초과... 🤬
