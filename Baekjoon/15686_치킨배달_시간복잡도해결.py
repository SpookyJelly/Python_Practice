import sys
sys.stdin = open('15686_input.txt','r')
from pprint import pprint
from itertools import combinations
from collections import deque

# 기본 아이디어는 훌륭했으나, 시간 초과 때문에 굉장히 화가난다.
# 시간 초과의 원인은 아마도 매 케이스마다 행렬을 직접 만드는 과정 때문일 것이다. 아니 100%이다
# 그러니까, 이번에는 행렬을 만들지 않고 해결하자
N,M = map(int,input().split())
KFC = [] # 치킨 집의 위치
home = [] # 도시에 있는 집 위치
city = [] # 도시 그 자체
for i in range(1,N+1):
    city_block = list(map(int,input().split()))
    for j in range(N):
        if city_block[j] == 1:
            home.append([i,j+1])
        elif city_block[j] == 2:
            KFC.append([i,j+1])
    city.append([0]+city_block)
city = [[0] *(N+1)] + city


survivor = combinations(KFC,M) # 살아남은 KFC들

# 도시의 최소 치킨 거리 == 임의의 큰 값
min_chicken_dis = 0xffffff
for s in survivor:
    # 각 조합에 대한 최소 치킨 거리 == 0으로 초기화
    result = 0
    for x,y in home:
        # 집마다 각 치킨집 대상으로 최소거리 조사 <- 최초에는 임의의 큰 값
        min_dis = 0xfffff
        for c_x,c_y in s:
            tem_min= abs(x-c_x)+abs(y-c_y)
            if tem_min <= min_dis:
                min_dis = tem_min
        # result = 집마다 갖는 최소 치킨 거리의 합
        result += min_dis
    # 도시의 최소 치킨 거리 = 각 조합에 대한 최소 치킨 거리 중 최소 값
    # 리스트로 append 받은 다음 최소값 구해도 되지만, 시간 초과가 계속 신경 쓰여서
    # 매 조합마다 최소값 비교로 정수형을 유지하기로 했다.
    min_chicken_dis = min(min_chicken_dis,result)


print(min_chicken_dis)