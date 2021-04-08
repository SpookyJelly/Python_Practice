#1012번 배추

# (한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

import sys
sys.stdin = open("1012_input.txt","r")

def eerie():
    global cnt
    # 델타 무브 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while insect:
        x,y = insect.pop(0)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 범위 안 벗어났으면 칠하자
            if 0<=new_x<M and 0<=new_y<N and area



T = int(input())

for _ in range(T):
    insect = []
    # M 가로 N 세로 K 배추의 갯수
    M,N,K = map(int,input().split())
    area = [[0]*M for _ in range(N)]
    print(area)
    for i in range(K):
        x,y = map(int,input().split())
        area[y][x] = 1
        insect.append([x,y])
    cnt = 0
    print(area)
    print(insect)
