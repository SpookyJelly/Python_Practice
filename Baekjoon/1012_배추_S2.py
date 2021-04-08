# 1012번 배추

# (한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

import sys

sys.stdin = open("1012_input.txt", "r")


def eerie():
    global cnt
    # 델타 무브 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    tem = []
    while insect:
        x1, y1 = insect.pop()
        tem.append([x1, y1])
        while tem:
            x, y = tem.pop()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                # 범위 안 벗어나고, 이동한 곳이 1이면.. 그리고 방문 까지 안했으면
                if 0 <= new_x < N and 0 <= new_y < M and area[new_x][new_y] and not visited[new_x][new_y]:
                    # 방문 처리 해주고, 큐 추가
                    visited[new_x][new_y] = True
                    if [new_x,new_y] in insect:
                        insect.remove([new_x, new_y])  # 삭제하고, 가장 먼저 탐색
                    tem.append([new_x, new_y])
        cnt += 1


T = int(input())

for _ in range(T):
    insect = []
    # M 가로 N 세로 K 배추의 갯수
    M, N, K = map(int, input().split())
    area = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        area[y][x] = 1
        insect.append([y, x])
    cnt = 0
    eerie()
    print(cnt)
