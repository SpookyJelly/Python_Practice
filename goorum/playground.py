# 놀이공원
# 가로 세로 Nkm인 정사각형 모양의 땅을 1km 단위로 영역 나누어 개별 판매중
# 가로세로 Kkm의 땅을 사야하는데, 그 안에 있는 쓰레기를 최소한으로 구하는 문제
# 1<=N<=100 / 1<=K <= 10 K<=N
import sys
sys.stdin = open('playground.txt', 'r')

TC = int(input())
for tc in range(TC):
    space = []
    N, K = map(int, input().split())
    for _ in range(N):
        tem = list(map(int, input().split()))
        space.append(tem)

    maxi = 0xfffffffff
    waste = 0
    for i in range(0, N-K+1):
        for j in range(0, N-K+1):
            for row in range(i, i+N-K+1):
                for col in range(j, j+N-K+1):
                    if space[row][col] == 1:
                        waste += 1

            if (waste <= maxi):
                maxi = waste
            waste = 0
    print(maxi)
