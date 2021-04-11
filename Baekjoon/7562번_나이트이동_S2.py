# #7562번 나이트 이동
#
# 입력
#
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
#
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다.
# 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
#
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

from collections import deque
import sys
sys.stdin = open('7562_input.txt','r')
#방문처리는 해야한다. 안그러면 무한 반복
def knight(start_x,start_y,level):
    # 델타 무브 : 10시 11시 1시 2시 4시 5시 7시 8시
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    que = deque([[start_x,start_y,level]])
    while que:
        x,y,level = que.popleft()
        # 뽑았는데 딱 정답인 경우도 있을수도 있잖아
        if (x, y) == (goal_x, goal_y):
            return level
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<l and 0<=new_y<l and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                if (new_x,new_y) == (goal_x,goal_y):
                    return level+1
                else:
                    que.append([new_x,new_y,level+1])
    return -1





TC = int(input())

for tc in range(TC):
    l = int(input()) # 체스판의 한변의 길이
    visited = [[False]*l for _ in range(l)] # 방문처리 체스판(목표 달성하려는 이상, 갔던 곳을 다시 갈 이유는 없다)
    start_x, start_y = map(int,input().split())
    goal_x, goal_y = map(int,input().split())
    print(knight(start_x,start_y,0))