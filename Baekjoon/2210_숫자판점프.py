# 2210 숫자판 점프
"""
문제
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

입력
다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.

출력
첫째 줄에 만들 수 있는 수들의 개수를 출력한다.

"""

import sys
sys.stdin = open('./2210_input.txt', 'r')


def bbs(x, y, string) -> None:
    if len(string) == 6:
        if string not in result:
            result.append(string)
        return
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 방문체크 생략
        if 0 <= nx < 5 and 0 <= ny < 5:
            bbs(nx, ny, string + arr[nx][ny])


arr = [list(input().split()) for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        string = ''
        bbs(i, j, string)

print(len(result))
