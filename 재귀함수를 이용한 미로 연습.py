#재귀 함수를 이용해서 미로 문제를 해결해보자


import sys
sys.stdin = open('maze.txt','r')


# 델타무브로 매 point를 개선해주는 방향을 고안하자.
# 그럼 visited 체크 해줘야하겠는데, 함수 밖에다가 행렬 만들어보자
def DFS_maze(point):
    global result

    (r,c) = point

    # 상하좌우
    dx= [-1,1,0,0]
    dy = [0,0,-1,1]
    if maze[r][c] == 3:
        result = 1  # 따로 변수 선언을 해줘서 도달했다고 표시를 해줘야하는데, global을 안쓰고 하는 방법은 없나?
        return


    for i in range(4):
        nr = r +dx[i]
        nc = c+ dy[i]

        if 0<=nr<N and 0<=nc<N and maze[nr][nc] != 1 and not visited[nr][nc]:
            visited[r][c] = True
            DFS_maze([nr,nc])
            # visited[nr][nc] = False
    # return result


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    maze =[]
    for i in range(N):
        tem = list(map(int,input()))
        if 2 in tem:
            start = [i,tem.index(2)]
        maze.append(tem)

    visited = [[False]*N for _ in range(N)]
    print(maze)
    result =0
    DFS_maze(start)
    print(result)

