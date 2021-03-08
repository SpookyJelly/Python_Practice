#2210 숫자판 점프

import sys
sys.stdin = open('2210_input.txt','r')


def bbs(x,y,string)->list:

    if len(string) == 6:
        if string not in result:
            result.append(string)
        return
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 방문체크 생략
        if 0<=nx<5 and 0<=ny<5:
            bbs (nx,ny,string+arr[nx][ny])



arr = [list(input().split()) for _ in range(5)]
result = []
for i in range(5):
    for j in range(5):
        string = ''
        bbs(i,j,string)

print(len(result))
