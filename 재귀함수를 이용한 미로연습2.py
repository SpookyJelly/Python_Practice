import sys

sys.stdin = open('1226_input.txt', 'r')


# 델타무브로 매 point를 개선해주는 방향을 고안하자.
# 그럼 visited 체크 해줘야하겠는데, 함수 밖에다가 행렬 만들어보자
def DFS_maze(point):
    global result

    (r, c) = point

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if maze[r][c] == '3' or result:
        result = 1  # 따로 변수 선언을 해줘서 도달했다고 표시를 해줘야하는데, global을 안쓰고 하는 방법은 없나?
        return

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != '1' and not visited[nr][nc]:
            visited[r][c] = True  # 현재 위치를 참으로 만들어준다
            # visited[nr][nc] = True # 다음 위치를 참으로 만들어준다. <-- 이것도 되긴 되네?? 어짜피 nr nc 돌면서
            # 이전의 현재값을 True로 만들어주니까 작동은 한다.
            # 그러나, 이전에 한번 왔던 곳을 다시 가서 다시 확인하는 절차이므로, 스택을 이용한 방법은 몰라도,
            # 재귀구현에서는 굉장히 불필요하고, 쓸데없는 낭비가 많을 것 같다. 그러니까, 현재 위치를 참으로 만들어주자.

            # maze[r][c] = 1 <-- visited 이용하기 싫으면, 현재 미료의 위치를 바꿔주는 방식으로 해도 괜찮다.
            DFS_maze([nr, nc])


# 아 시발 이거 왜 안되나 했는데....자료형 문제였네

for _ in range(10):
    tc = int(input())
    maze = []
    N = 16
    for i in range(N):
        tem = list(input())
        if '2' in tem:
            start = [i, tem.index('2')]
        maze.append(tem)

    visited = [[False] * N for _ in range(N)]

    result = 0
    DFS_maze(start)
    print('#{} {}'.format(tc,result))
